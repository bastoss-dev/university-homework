#!/usr/bin/env python3
"""Gera relatório final em PDF com os artefatos efetivamente publicados no repositório."""
from pathlib import Path
from xml.sax.saxutils import escape
from datetime import date
from PIL import Image as PIL
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

BASE=Path(__file__).resolve().parents[1]
OUT=BASE/"docs"/"relatorio-final.pdf"
OUT.parent.mkdir(exist_ok=True)
NAVY=colors.HexColor("#202642")
PURPLE=colors.HexColor("#6d5df6")
GRAY=colors.HexColor("#64708b")
LINE=colors.HexColor("#e7e9f2")
PALE=colors.HexColor("#f5f5fb")
try:
    pdfmetrics.registerFont(TTFont("DejaVu","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
    pdfmetrics.registerFont(TTFont("DejaVu-Bold","/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
    normal,bold="DejaVu","DejaVu-Bold"
except Exception:
    normal,bold="Helvetica","Helvetica-Bold"
styles={
"body":ParagraphStyle("Body",fontName=normal,fontSize=9,leading=15,textColor=NAVY,spaceAfter=8),
"small":ParagraphStyle("Small",fontName=normal,fontSize=7.7,leading=12,textColor=GRAY,spaceAfter=7),
"h1":ParagraphStyle("H1",fontName=bold,fontSize=16,leading=23,textColor=NAVY,spaceBefore=13,spaceAfter=12,keepWithNext=True),
"h2":ParagraphStyle("H2",fontName=bold,fontSize=11.2,leading=17,textColor=PURPLE,spaceBefore=11,spaceAfter=7,keepWithNext=True),
"table":ParagraphStyle("Table",fontName=normal,fontSize=7.5,leading=11,textColor=NAVY),
"th":ParagraphStyle("TH",fontName=bold,fontSize=7.5,leading=11,textColor=colors.white),
"cap":ParagraphStyle("Caption",fontName=normal,fontSize=8,leading=12,textColor=GRAY,alignment=TA_CENTER,spaceBefore=5,spaceAfter=16),
"cover":ParagraphStyle("Cover",fontName=bold,fontSize=34,leading=45,textColor=NAVY,alignment=TA_CENTER),
"center":ParagraphStyle("Center",fontName=normal,fontSize=12,leading=21,textColor=GRAY,alignment=TA_CENTER),
}
pdf=SimpleDocTemplate(str(OUT),pagesize=A4,leftMargin=1.8*cm,rightMargin=1.8*cm,topMargin=1.9*cm,bottomMargin=1.85*cm,
 title="Foco Tarefas — Relatório Final de Engenharia de Software",author="Yuri Fernandes Bastos")
W=A4[0]-pdf.leftMargin-pdf.rightMargin
story=[]
def p(s,style="body"):story.append(Paragraph(s,styles[style]))
def section(n,title):
    p(str(n)+". "+title,"h1")
    story.append(HRFlowable(width="100%",thickness=0.7,color=LINE,spaceAfter=10))
def sub(s):p(s,"h2")
def bullet(s):p("&#8226; "+s)
def table(head,rows, widths):
    arr=[[Paragraph(str(x),styles["th"]) for x in head]]
    for row in rows:arr.append([Paragraph(escape(str(x)),styles["table"]) for x in row])
    t=Table(arr,colWidths=widths,repeatRows=1,hAlign="LEFT")
    t.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),NAVY),("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,PALE]),
     ("VALIGN",(0,0),(-1,-1),"TOP"),("GRID",(0,0),(-1,-1),0.35,LINE),("LEFTPADDING",(0,0),(-1,-1),8),
     ("RIGHTPADDING",(0,0),(-1,-1),7),("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7)]))
    story.append(t);story.append(Spacer(1,14))
def pic(path,caption,mw=W,mh=9*cm):
    filename=BASE/path
    if not filename.exists():raise FileNotFoundError(filename)
    with PIL.open(filename) as img:w,h=img.size
    factor=min(mw/w,mh/h)
    story.append(Image(str(filename),width=w*factor,height=h*factor))
    p(caption,"cap")

repo="https://github.com/bastoss-dev/university-homework/tree/main/foco-tarefas"
board="https://github.com/bastoss-dev/university-homework/blob/main/foco-tarefas/docs/planejamento/quadro-online.md"
issues="https://github.com/bastoss-dev/university-homework/issues?q=is%3Aissue+%22Foco+Tarefas%22"
story.extend([Spacer(1,2.2*cm)])
p("UNIMA — CENTRO UNIVERSITÁRIO DE MACEIÓ","center")
story.extend([Spacer(1,1.1*cm)])
p("PROJETO FINAL — ENGENHARIA DE SOFTWARE","center")
story.extend([Spacer(1,1.4*cm)])
p("FOCO<br/>TAREFAS","cover")
story.extend([Spacer(1,.5*cm)])
p("Sistema de gerenciamento de tarefas pessoais","center")
story.extend([Spacer(1,1.2*cm)])
p("Planejamento · Requisitos · UML · Prototipação<br/>Desenvolvimento · Testes · Documentação","center")
story.extend([Spacer(1,1.7*cm)])
p("<b>Integrante único:</b> Yuri Fernandes Bastos","center")
p("Maceió — AL · 09/11/2026","center")
story.append(PageBreak())

section(1,"Identificação")
p("<b>Projeto:</b> Foco Tarefas. <b>Disciplina:</b> Engenharia de Software. <b>Instituição:</b> UNIMA — Centro Universitário de Maceió.")
p("<b>Integrante e responsável:</b> Yuri Fernandes Bastos (único integrante).")
p("<b>Tipo:</b> aplicação web local, responsiva e executável sem servidor. <b>Prazo de entrega:</b> 13/11/2026.")
p("<b>Materiais:</b> código-fonte, README, quadro de gestão em GitHub, requisitos, dois diagramas UML, três protótipos, imagens do sistema e testes.")

section(2,"Introdução")
sub("Problema")
p("Tarefas de estudo, trabalho e rotina frequentemente ficam dispersas em diferentes anotações. A falta de um único local dificulta identificar pendências, estabelecer prioridades e avaliar o progresso.")
sub("Justificativa e objetivo")
p("O Foco Tarefas propõe uma solução de baixa complexidade que permite cadastrar, consultar, editar, concluir, excluir e organizar atividades. O objetivo acadêmico é aplicar de modo articulado as etapas de Engenharia de Software.")
sub("Público-alvo e escopo")
p("<b>Público-alvo:</b> estudantes e pessoas que precisam gerenciar atividades individuais. <b>Stakeholders:</b> usuário final, responsável pelo projeto e professor avaliador.")
p("<b>Incluído:</b> CRUD, categorias, prioridades, datas, busca, filtros, indicadores e backup JSON. <b>Excluído:</b> login, sincronização em nuvem, colaboração em tempo real e notificações.")

section(3,"Planejamento e gerenciamento")
sub("Modelo incremental")
p("O desenvolvimento seguiu um modelo incremental: (1) problema e requisitos; (2) diagramas UML e protótipos; (3) implementação das funções essenciais; (4) testes e documentação. A abordagem foi escolhida por reduzir o risco de um sistema acadêmico pequeno.")
table(["Incremento","Atividades e entregas"],[
["1 - Planejamento","Definição do objetivo, stakeholders, requisitos e escopo."],
["2 - Modelagem","Casos de uso, classes e três telas prototipadas."],
["3 - Desenvolvimento","Interface HTML/CSS, regras JavaScript, CRUD e persistência local."],
["4 - Validação","Testes de lógica e interface, capturas, README e relatório."]
],[W*.27,W*.73])
sub("Ferramenta de acompanhamento")
p("O acompanhamento do projeto está registrado no <b>GitHub Issues</b>, com 13 itens numerados e atribuídos ao integrante Yuri Fernandes Bastos. O quadro Markdown publicado no repositório os distribui nas colunas <b>A fazer, Em andamento, Em testes e Concluído</b>, com links para as issues. O histórico de cada issue permite identificar estados e responsabilidades.")
p("<b>Quadro publicado:</b> <link href='"+board+"'>ver quadro de acompanhamento</link>. <b>Issues:</b> <link href='"+issues+"'>ver atividades e histórico</link>.")
pic("docs/capturas/04-quadro-kanban.png","Figura 1 — Visualização HTML do acompanhamento registrado em GitHub Issues; não é um quadro Trello.",mh=8.1*cm)

section(4,"Engenharia de requisitos")
sub("Técnica de identificação de necessidades")
p("Foi empregada análise do problema com observação estruturada de <b>cenários simulados</b>: criar tarefa, localizar uma pendência, alterar prioridade e marcar conclusão. Não foram realizadas entrevistas ou questionários reais.")
sub("Requisitos funcionais")
table(["Código","Descrição","Feito"],[
["RF01","Cadastrar tarefas com título obrigatório e demais campos.","Sim"],
["RF02","Listar tarefas cadastradas.","Sim"],
["RF03","Editar tarefa existente.","Sim"],
["RF04","Excluir tarefa após confirmação.","Sim"],
["RF05","Alterar status e marcar/desfazer conclusão.","Sim"],
["RF06","Pesquisar e filtrar por status/categoria.","Sim"],
["RF07","Exibir indicadores e percentual de progresso.","Sim"],
["RF08","Importar e exportar arquivos de backup JSON.","Sim"],
],[W*.14,W*.72,W*.14])
sub("Requisitos não funcionais")
table(["Código","Descrição","Feito"],[
["RNF01","Layout responsivo para desktop e celular.","Sim"],
["RNF02","Execução local e persistência no navegador.","Sim"],
["RNF03","Validação de campos e mensagens claras de erro.","Sim"],
],[W*.14,W*.72,W*.14])

section(5,"Modelagem UML")
p("A modelagem contém um diagrama de casos de uso (ator Usuário e ações sobre tarefas) e um diagrama de classes (Tarefa, TaskManager e dependência de armazenamento), ambos relacionados ao código.")
sub("Diagrama de casos de uso")
pic("docs/uml/casos-de-uso.png","Figura 2 — Casos de uso do sistema.",mw=W*.9,mh=11*cm)
sub("Diagrama de classes")
pic("docs/uml/classes.png","Figura 3 — Classes e dependências da implementação.",mw=W,mh=9.5*cm)

section(6,"Prototipação")
p("Foram preparados três protótipos de baixa fidelidade antes da versão final da interface, representando a navegação e a distribuição dos controles.")
sub("Tela 1 — Painel")
pic("docs/prototipos/01-painel.png","Figura 4 — Protótipo do painel, vinculado aos requisitos RF02 e RF07.",mh=7.6*cm)
sub("Tela 2 — Listagem")
pic("docs/prototipos/02-lista.png","Figura 5 — Protótipo da consulta e filtros, requisitos RF02 a RF06.",mh=7.6*cm)
sub("Tela 3 — Formulário")
pic("docs/prototipos/03-formulario.png","Figura 6 — Protótipo do cadastro e edição, requisitos RF01 e RF03.",mh=7.6*cm)

section(7,"Desenvolvimento do software")
sub("Arquitetura e tecnologias")
p("O sistema utiliza <b>HTML5</b>, <b>CSS3</b>, <b>JavaScript</b> e <b>localStorage</b>. A classe TaskManager centraliza validação, persistência e CRUD; os arquivos CSS e JavaScript separados permitem manutenção, além de uma versão independente em arquivo HTML.")
p("A aplicação não depende de instalação, servidor externo nem conexão de internet para uso normal. O repositório traz o código-fonte e o passo a passo de execução no README.")
sub("Funcionalidades implementadas e interface")
p("As oito funções contemplam cadastro, consulta, edição, exclusão, mudança de status, pesquisa e filtros, estatísticas e backups JSON. As capturas abaixo foram produzidas com dados fictícios em navegador automatizado.")
pic("docs/capturas/01-painel.png","Figura 7 — Tela real do painel de indicadores.",mh=8.5*cm)
pic("docs/capturas/02-lista.png","Figura 8 — Tela real de listagem e consulta.",mh=8.5*cm)
pic("docs/capturas/03-cadastro.png","Figura 9 — Tela real do formulário de tarefa.",mh=8.5*cm)

section(8,"Testes e validação")
sub("Execução automatizada")
p("A suíte Node.js (node:test) cobre dez cenários de regras de negócio; a automação visual Playwright/Chromium executa doze verificações de interface. Os registros são armazenados em <b>docs/resultado-testes-node.txt</b> e <b>docs/evidencias-testes-ui.txt</b>.")
table(["ID","Procedimento","Esperado","Obtido","Situação"],[
["CT01","Cadastrar tarefa válida","Incluir na lista","Registro incluído","Aprovado"],
["CT02","Pesquisar e filtrar tarefas","Somente resultados","Filtro aplicado","Aprovado"],
["CT03","Editar uma tarefa","Dados alterados","Dados alterados","Aprovado"],
["CT04","Concluir uma de duas tarefas","50% de progresso","50% de progresso","Aprovado"],
["CT05","Excluir registro existente","Registro removido","Registro removido","Aprovado"],
["CT06","Cadastrar título vazio","Bloquear ação","Cadastro bloqueado","Aprovado"],
["CT07","Exportar/importar JSON","Restaurar tarefas","Tarefa recuperada","Aprovado"],
["CT08","Importar JSON inválido","Rejeitar arquivo","Arquivo rejeitado","Aprovado"],
["CT09","Prioridade inválida","Rejeitar dados","Dados rejeitados","Aprovado"],
["CT10","Reabrir gerenciador","Recuperar dados","Dados recuperados","Aprovado"]
],[W*.105,W*.31,W*.205,W*.23,W*.15])
p("As verificações UI01–UI12 também abrangem painel, listagem, busca, filtro, cadastro, persistência após recarregar a página, edição, conclusão, exclusão, exportação, erros de JavaScript e largura móvel.")
pic("docs/capturas/05-mobile.png","Figura 10 — Responsividade da interface em 390 pixels.",mw=W*.5,mh=10*cm)

section(9,"Considerações finais")
p("O projeto demonstrou que a Engenharia de Software abrange análise de necessidades, planejamento, modelagem, protótipos, implementação, testes e documentação, além da programação. O produto final permanece simples e tem operações funcionais ligadas aos requisitos.")
p("<b>Dificuldades abordadas:</b> validação de dados importados, ligação entre interface e armazenamento, estados das tarefas e consistência dos testes. <b>Limitações:</b> sem contas, nuvem ou colaboração. <b>Melhorias futuras:</b> login, alertas de prazos, sincronização e relatórios.")

section(10,"Repositório e entrega")
p("<b>Repositório GitHub:</b> <link href='"+repo+"'>"+escape(repo)+"</link>.")
p("<b>Quadro de gerenciamento:</b> <link href='"+board+"'>"+escape(board)+"</link>.")
p("<b>GitHub Issues:</b> <link href='"+issues+"'>atividades atribuídas e histórico</link>.")
p("<b>Responsável único:</b> Yuri Fernandes Bastos.")
p("<b>Para executar:</b> baixar o repositório e abrir <b>index.html</b> no navegador. Para executar testes de regra: <b>node --test tests/core.test.js</b>.")
p("<b>Entrega:</b> até 13/11/2026 pelo Canvas, com este PDF e os links solicitados. A conferência final no computador do aluno e a submissão pelo Canvas não são realizadas pela automação.")
p("A produção técnica e editorial contou com assistência automatizada. O estudante identificado deve conferir conteúdo, integridade e conformidade acadêmica antes de entregar.","small")

def header(c,doc):
    c.saveState()
    c.setStrokeColor(LINE)
    c.line(1.8*cm,A4[1]-1.25*cm,A4[0]-1.8*cm,A4[1]-1.25*cm)
    c.line(1.8*cm,1.44*cm,A4[0]-1.8*cm,1.44*cm)
    c.setFont(normal,7.5)
    c.setFillColor(GRAY)
    c.drawString(1.8*cm,1.1*cm,"UNIMA  |  Engenharia de Software  |  Yuri Fernandes Bastos")
    c.drawRightString(A4[0]-1.8*cm,1.1*cm,str(doc.page))
    c.restoreState()
pdf.build(story,onFirstPage=header,onLaterPages=header)
print(f"PDF gerado: {OUT}, {OUT.stat().st_size} bytes")
