# Foco Tarefas — Projeto Final de Engenharia de Software

**Foco Tarefas** é um gerenciador de tarefas pessoais desenvolvido como projeto acadêmico da UNIMA (Maceió). A aplicação foi feita em **HTML, CSS e JavaScript**, roda no navegador e armazena dados localmente.

## Como executar

1. Baixe o arquivo [index.html](index.html).
2. Abra-o no Chrome, Edge ou Firefox.
3. Clique em **Nova tarefa**, cadastre uma tarefa e consulte em **Minhas tarefas**.

**Não requer instalação, servidor, Node.js ou conexão com a internet.** O arquivo `index.html` publicado nesta pasta é independente e inclui HTML, CSS e JavaScript.

## Problema e funcionalidades

O sistema concentra tarefas acadêmicas, profissionais e pessoais para que o usuário organize atividades, acompanhe prioridades e veja o progresso.

- Criar e listar tarefas.
- Editar e excluir com confirmação.
- Alterar status e concluir/reabrir tarefas.
- Pesquisar e filtrar por status e categoria.
- Consultar indicadores e progresso.
- Importar e exportar backup JSON.
- Armazenar tarefas com `localStorage` no navegador.

## Engenharia de Software

- [Requisitos funcionais e não funcionais](docs/requisitos.md).
- [UML — casos de uso (PlantUML)](docs/uml/casos-de-uso.puml).
- [UML — classes (PlantUML)](docs/uml/classes.puml).
- Três protótipos de baixa fidelidade:
  - [Tela 1 — painel](docs/prototipos/01-painel.svg)
  - [Tela 2 — lista](docs/prototipos/02-lista.svg)
  - [Tela 3 — cadastro](docs/prototipos/03-formulario.svg)
- [Casos de teste e resultados](docs/testes.md).
- [Arquivo de planejamento em CSV](docs/planejamento/tarefas.csv).
- [Descrição da metodologia incremental](docs/planejamento/README.md).
- [Gerenciamento das etapas no GitHub Issues](https://github.com/bastoss-dev/university-homework/issues?q=is%3Aissue+%22Foco+Tarefas%22).

**Importante:** o pacote completo originalmente disponibilizado na conversa contém relatório PDF, capturas do sistema, fontes modularizadas, protótipos originais, diagramas em PNG e testes automatizados. O conteúdo desta pasta do GitHub é uma **publicação simplificada e executável**, não a cópia integral de todos os anexos do pacote.

## Planejamento e testes

Foi adotada uma abordagem incremental, passando por planejamento, requisitos, modelagem, prototipação, desenvolvimento e validação. Os itens estão registrados no GitHub Issues, identificados pelo nome **Foco Tarefas**, com estados em seus títulos. Os responsáveis reais devem ser definidos pelos integrantes; as atividades preparadas por assistência automatizada não devem ser atribuídas indevidamente a estudantes.

Durante a preparação do pacote completo foram reportados **10 testes automatizados de lógica** e **12 verificações de interface** aprovados; os scripts e registros encontram-se no pacote completo. Teste a versão baixada manualmente no seu navegador antes da entrega.

## Integrantes

**[PREENCHER NOMES REAIS DOS INTEGRANTES]**

## Entrega

- **Disciplina:** Engenharia de Software.
- **Instituição:** UNIMA — Centro Universitário de Maceió.
- **Prazo:** 13/11/2026.
- **Relatório PDF:** disponível no pacote completo disponibilizado ao aluno, ainda não publicado neste repositório.
- **GitHub:** https://github.com/bastoss-dev/university-homework/tree/main/foco-tarefas
- **Quadro externo:** o Trello ainda depende de conexão; a [aba Issues](https://github.com/bastoss-dev/university-homework/issues) possui o acompanhamento inicial, mas não substitui automaticamente um quadro Trello/GitHub Projects configurado e documentado.
- **Entrega Canvas:** deve ser feita pelo aluno ou representante da equipe.

## Limitações

Os dados são guardados no navegador (sem sincronização entre dispositivos); não há autenticação, banco remoto, notificações ou compartilhamento em tempo real. Essas são possibilidades de evolução.
