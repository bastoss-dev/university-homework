# Foco Tarefas ✦

![Tela inicial do Foco Tarefas](docs/capturas/01-painel.png)

**Foco Tarefas** é um gerenciador de tarefas pessoais desenvolvido como projeto final de Engenharia de Software da UNIMA (Maceió). Seu objetivo é ajudar estudantes e outros usuários a organizar tarefas, definir prioridades e acompanhar o progresso de atividades cotidianas.

## Problema que resolve

Muitas atividades de estudo, trabalho e vida pessoal são controladas de forma dispersa. Isso dificulta identificar prioridades, localizar pendências e avaliar o próprio progresso. O Foco reúne as tarefas em uma interface simples, com indicadores, filtros e armazenamento local.

## Integrantes da equipe

**[PREENCHER NOME(S) DOS INTEGRANTES ANTES DA ENTREGA]**

As contribuições de cada integrante devem ser registradas no quadro de gerenciamento externo e/ou no histórico do GitHub. Não atribuir autoria a pessoas que não participaram.

## Tecnologias utilizadas

- **HTML5** para estruturar as telas.
- **CSS3** para layout responsivo.
- **JavaScript** para as funcionalidades, validação e manipulação dos registros.
- **Web Storage API (localStorage)** para persistir as tarefas neste navegador.
- **Node.js** (apenas para executar os testes automatizados, não é requisito para abrir o programa).
- **Graphviz/PlantUML** para produzir e manter os diagramas de modelagem.
- **Python/ReportLab** para gerar o relatório técnico a partir dos artefatos.

## Funcionalidades

1. Cadastrar tarefas com título, descrição, categoria, prioridade, status e data limite.
2. Listar todas as tarefas cadastradas.
3. Editar tarefas existentes.
4. Excluir tarefas, com confirmação.
5. Marcar tarefas como concluídas (e desfazer a conclusão).
6. Buscar por título/descrição e filtrar por status/categoria.
7. Visualizar indicadores: total, pendentes, em andamento, concluídas e percentual de conclusão.
8. Exportar e importar backup de tarefas em JSON.

## Como abrir

**Não precisa instalar nada nem executar um servidor.**

1. Baixe ou clone o repositório, mantendo as pastas `css` e `js` junto com `index.html`.
2. Abra o arquivo **`index.html`** no Google Chrome, Microsoft Edge ou outro navegador moderno.
3. Use **Nova tarefa** para cadastrar uma atividade.
4. Acesse **Minhas tarefas** para editar, concluir, excluir e filtrar.

**Alternativa:** use o arquivo independente `Foco_Tarefas_Abrir.html` entregue junto com o pacote. Ele inclui o código e o estilo em um único arquivo.

Observações: os dados ficam no `localStorage` do navegador em que o sistema foi aberto. Mudar de navegador, limpar os dados do site ou acessar o arquivo de outro local pode afetar os registros. Faça backups usando **Exportar JSON**. O programa não depende de internet, banco de dados externo nem autenticação.

## Testes

Testes automatizados de regras do sistema (é necessário Node.js apenas para este comando):

```bash
node --test tests/core.test.js
```

**Validação realizada em 09/11/2026:** 10 testes automatizados de lógica (aprovados) e 12 verificações de interface (aprovadas), incluindo cadastro, filtros, edição, status, exclusão e responsividade. As evidências estão em `docs/evidencias-testes-ui.txt` e no relatório em PDF. A automação visual no ambiente de geração utilizou uma implementação em memória da interface de Storage, devido a restrições locais de navegação do navegador de testes; não substitui a verificação manual no computador do aluno.

## Diagramas UML

- [Casos de uso (PNG)](docs/uml/casos-de-uso.png) · [fonte PlantUML](docs/uml/casos-de-uso.puml)
- [Classes (PNG)](docs/uml/classes.png) · [fonte PlantUML](docs/uml/classes.puml)

## Protótipos de interface

Os três protótipos de baixa fidelidade estão em `docs/prototipos/`:

| Visão geral | Lista | Formulário |
|---|---|---|
| ![Protótipo do painel](docs/prototipos/01-painel.png) | ![Protótipo da lista](docs/prototipos/02-lista.png) | ![Protótipo do formulário](docs/prototipos/03-formulario.png) |

## Capturas do sistema

![Lista de tarefas](docs/capturas/02-lista.png)

![Formulário](docs/capturas/03-cadastro.png)

Imagens ilustrativas, com tarefas fictícias, registradas a partir do sistema implementado.

## Organização do projeto

```text
foco-tarefas/
├── index.html                 # Aplicação principal
├── css/styles.css             # Estilos
├── js/core.js                 # Regras de tarefas e persistência
├── js/app.js                  # Interface e eventos
├── tests/core.test.js         # 10 testes automatizados
├── dados-projeto.json         # Nomes e links a preencher
├── docs/
│   ├── relatorio-final.pdf    # Relatório técnico
│   ├── uml/                   # 2 diagramas UML (PNG, SVG, DOT e PUML)
│   ├── prototipos/            # 3 wireframes, HTML e imagens
│   ├── capturas/              # Imagens reais do sistema e quadro
│   ├── planejamento/          # Kanban local, CSV, instruções
│   └── evidencias-testes-ui.txt
└── scripts/                   # Geradores e testes visuais auxiliares
```

## Metodologia e acompanhamento

O processo foi organizado em incrementos, com fases de planejamento/requisitos, modelagem/prototipação, implementação e testes/documentação. Os cartões de trabalho estão em [quadro Kanban local](docs/planejamento/quadro-kanban.html), e a tabela para migração ao Trello/GitHub Projects está em [tarefas.csv](docs/planejamento/tarefas.csv).

**Quadro online:** planejamento por GitHub Issues nesta pasta/repositório; consultar a aba Issues. O Trello depende de conexão externa.

![Quadro Kanban local](docs/capturas/04-quadro-kanban.png)

**Nota:** o Kanban em HTML é um quadro local e editável, não um quadro público publicado no Trello. Para satisfazer integralmente a exigência de comprovação por link, crie o quadro em Trello/GitHub Projects, defina responsáveis reais, registre evidências e substitua o campo acima pelo endereço correto.

## Relatório técnico

Leia [docs/relatorio-final.pdf](docs/relatorio-final.pdf). O relatório segue as dez seções previstas no enunciado. O arquivo `dados-projeto.json` reúne os campos que dependem da equipe e da publicação externa. Para gerar novamente o PDF, execute `python scripts/gerar_relatorio.py` (requer ReportLab e Pillow).

## Repositório GitHub

**https://github.com/bastoss-dev/university-homework/tree/main/foco-tarefas**

O pacote já está organizado para publicação. Caso utilize a interface web do GitHub, crie um repositório e envie o conteúdo desta pasta, mantendo os diretórios. Caso use Git instalado, na pasta raiz do projeto:

```bash
git init
git add .
git commit -m "Entrega do projeto Foco Tarefas"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
git push -u origin main
```

Substitua a URL ilustrativa pelo endereço criado **de verdade** antes de executar. Esta pasta foi publicada no repositório acadêmico do GitHub.

## Entrega acadêmica

**Prazo definido no enunciado:** 13/11/2026, pelo Canvas. Enviar o PDF do relatório, o link real do GitHub e o link real do quadro de gerenciamento. Confirmar os nomes dos integrantes. O Canvas e as contas externas não foram acessados durante a criação destes arquivos.

## Limitações e melhorias

Esta versão é um protótipo funcional de uso local e individual: não oferece contas, sincronização entre dispositivos, colaboração, alertas ou banco de dados remoto. Melhorias futuras podem incluir notificações, autenticação, banco em nuvem e categorização customizada.