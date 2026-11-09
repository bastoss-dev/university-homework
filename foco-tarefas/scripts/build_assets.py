#!/usr/bin/env python3
"""Gera capturas reais do Foco Tarefas (Chromium) e converte UML/protótipos SVG em PNG."""
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from playwright.sync_api import sync_playwright
import cairosvg

BASE = Path(__file__).resolve().parents[1]
CAP = BASE / "docs" / "capturas"
CAP.mkdir(parents=True, exist_ok=True)

for folder in ["uml", "prototipos"]:
    for src in sorted((BASE / "docs" / folder).glob("*.svg")):
        cairosvg.svg2png(url=str(src), write_to=str(src.with_suffix(".png")), output_width=1280)

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        return

server=ThreadingHTTPServer(("127.0.0.1",0),partial(Quiet,directory=str(BASE)))
Thread(target=server.serve_forever,daemon=True).start()
address=f"http://127.0.0.1:{server.server_address[1]}"
checks=[]
records=[
{"title":"Finalizar projeto de Engenharia de Software","description":"Conferir relatório e organizar arquivos","category":"Estudos","priority":"Alta","status":"Em andamento","dueDate":"2026-11-13"},
{"title":"Revisar conteúdo da disciplina","description":"Rever requisitos e UML","category":"Estudos","priority":"Alta","status":"Pendente","dueDate":"2026-11-11"},
{"title":"Organizar cronograma da semana","description":"Planejar atividades","category":"Pessoal","priority":"Média","status":"Pendente","dueDate":"2026-11-14"},
{"title":"Estudar para a avaliação","description":"Conferir material","category":"Estudos","priority":"Baixa","status":"Concluída","dueDate":"2026-11-08"},
{"title":"Revisar lista de tarefas","description":"Conferir pendências","category":"Trabalho","priority":"Média","status":"Concluída","dueDate":"2026-11-09"}
]
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,args=["--no-sandbox"])
    context=browser.new_context(viewport={"width":1440,"height":960},device_scale_factor=1,accept_downloads=True)
    page=context.new_page()
    errors=[]
    page.on("pageerror",lambda err:errors.append(str(err)))
    page.goto(address+"/index.html",wait_until="load")
    page.evaluate("(items)=>{for(const x of items)window.__focoApp.manager.create(x);window.__focoApp.render();}",records)
    assert page.locator(".stat-card strong").first.inner_text()=="5"
    checks.append("UI01 - Painel apresenta 5 tarefas e indicadores: APROVADO")
    page.screenshot(path=str(CAP/"01-painel.png"),full_page=True)
    page.evaluate("location.hash='#tarefas'")
    assert page.locator(".task-row").count()==5
    checks.append("UI02 - Lista apresenta 5 tarefas: APROVADO")
    page.screenshot(path=str(CAP/"02-lista.png"),full_page=True)
    page.locator("#search-tasks").fill("disciplina")
    assert page.locator(".task-row").count()==1
    checks.append("UI03 - Pesquisa filtra por texto: APROVADO")
    page.locator("#search-tasks").fill("")
    page.locator("#filter-status").select_option("Concluída")
    assert page.locator(".task-row").count()==2
    checks.append("UI04 - Filtro de status funciona: APROVADO")
    page.locator("#filter-status").select_option("Todas")
    page.evaluate("location.hash='#nova'")
    page.screenshot(path=str(CAP/"03-cadastro.png"),full_page=True)
    page.locator("#task-title").fill("Testar aplicativo")
    page.locator("#task-category").select_option("Trabalho")
    page.locator("#task-priority").select_option("Alta")
    page.locator("#task-form button[type='submit']").click()
    assert page.locator(".task-row").count()==6
    checks.append("UI05 - Cadastro de tarefa funciona: APROVADO")
    page.reload()
    page.evaluate("location.hash='#tarefas'")
    assert page.locator(".task-row").count()==6
    checks.append("UI06 - Persistência REAL em localStorage após recarga: APROVADO")
    item=page.locator(".task-row").filter(has_text="Testar aplicativo")
    item.locator('[data-action="edit"]').click()
    page.locator("#task-title").fill("Testar aplicativo no Chromium")
    page.locator("#task-form button[type='submit']").click()
    assert page.locator(".task-row").filter(has_text="Testar aplicativo no Chromium").count()==1
    checks.append("UI07 - Edição funciona: APROVADO")
    item=page.locator(".task-row").filter(has_text="Testar aplicativo no Chromium")
    item.locator('[data-action="toggle"]').check()
    assert "Concluída" in page.locator(".task-row").filter(has_text="Testar aplicativo no Chromium").inner_text()
    checks.append("UI08 - Mudança de status funciona: APROVADO")
    page.once("dialog",lambda dialog:dialog.accept())
    page.locator(".task-row").filter(has_text="Testar aplicativo no Chromium").locator('[data-action="delete"]').click()
    assert page.locator(".task-row").count()==5
    checks.append("UI09 - Exclusão funciona: APROVADO")
    with page.expect_download() as dl:
        page.locator("#export-btn").click()
    assert dl.value.suggested_filename.endswith(".json")
    checks.append("UI10 - Download de backup JSON funciona: APROVADO")
    assert not errors, "Erros de JS: "+repr(errors)
    checks.append("UI11 - Nenhum erro de JavaScript: APROVADO")
    board=context.new_page(viewport={"width":1580,"height":900})
    board.goto(address+"/docs/planejamento/quadro-kanban.html")
    board.screenshot(path=str(CAP/"04-quadro-kanban.png"),full_page=True)
    board.close()
    mcontext=browser.new_context(viewport={"width":390,"height":844})
    mobile=mcontext.new_page()
    mobile.goto(address+"/index.html")
    assert mobile.evaluate("document.documentElement.scrollWidth")<=390
    checks.append("UI12 - Layout de 390px sem rolagem horizontal: APROVADO")
    mobile.screenshot(path=str(CAP/"05-mobile.png"),full_page=True)
    mcontext.close()
    context.close()
    browser.close()
server.shutdown()
summary=("VALIDAÇÃO FUNCIONAL NO CHROMIUM COM NAVEGADOR REAL E LOCALSTORAGE REAL\n"+
         "Execução automatizada em GitHub Actions (a data é a data da execução do workflow).\n\n"+
         "\n".join(checks)+"\n\nResultado: 12 verificações aprovadas, dados de exemplo fictícios.\n")
(BASE/"docs"/"evidencias-testes-ui.txt").write_text(summary,encoding="utf-8")
print(summary)
