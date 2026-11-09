# Engenharia de Requisitos — Foco Tarefas
**Problema:** acompanhar pendências acadêmicas, pessoais e profissionais em um único local.

**Objetivo:** permitir ao usuário cadastrar, consultar e acompanhar suas tarefas.

**Stakeholders:** usuário final, equipe de desenvolvimento e professor avaliador.

**Técnica de levantamento:** observação estruturada de cenários simulados. Não houve entrevistas com usuários reais.

| ID | Requisito funcional | Implementado |
|---|---|---|
| RF01 | Cadastrar tarefas com título e outros dados | Sim |
| RF02 | Listar tarefas | Sim |
| RF03 | Editar tarefas cadastradas | Sim |
| RF04 | Excluir tarefas após confirmação | Sim |
| RF05 | Alterar status e concluir/reabrir tarefas | Sim |
| RF06 | Filtrar por status/categoria e pesquisar por texto | Sim |
| RF07 | Visualizar indicadores de progresso | Sim |
| RF08 | Exportar e importar backup em JSON | Sim |

| ID | Requisito não funcional | Implementado |
|---|---|---|
| RNF01 | Interface responsiva | Sim |
| RNF02 | Execução local/offline e persistência local | Sim |
| RNF03 | Validação de campos e mensagens compreensíveis | Sim |

**Escopo excluído:** autenticação, nuvem, colaboração em tempo real e alertas.
