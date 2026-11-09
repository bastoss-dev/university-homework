# Testes do Foco Tarefas

**Suíte de lógica:** Node.js `node:test` — `node --test tests/core.test.js`.
**Suíte de interface:** Playwright/Chromium com servidor HTTP local, localStorage real e reinicialização de página.
**Responsável acadêmico:** Yuri Fernandes Bastos.

| Caso | Funcionalidade | Procedimento | Resultado esperado | Resultado obtido | Situação |
|---|---|---|---|---|---|
| CT01 | Cadastro | Cadastrar título válido | Registro adicionado | Registro listado | Aprovado |
| CT02 | Pesquisa e filtro | Consultar por texto e categoria | Somente correspondências | Filtro correto | Aprovado |
| CT03 | Edição | Atualizar dados existentes | Alterações persistidas | Alteração refletida | Aprovado |
| CT04 | Conclusão | Concluir uma de duas tarefas | Progresso de 50% | 50% | Aprovado |
| CT05 | Exclusão | Excluir tarefa | Registro removido | Registro removido | Aprovado |
| CT06 | Validação | Título vazio | Impedir cadastro | Cadastro bloqueado | Aprovado |
| CT07 | Backup | Exportar/importar JSON | Tarefa restaurada | Restaurada | Aprovado |
| CT08 | Arquivo inválido | Importar JSON sem tasks | Recusar documento | Importação recusada | Aprovado |
| CT09 | Campo inválido | Prioridade não permitida | Recusar valor | Valor recusado | Aprovado |
| CT10 | Persistência | Instanciar outro gerenciador | Consultar tarefa existente | Tarefa recuperada | Aprovado |

**Outras verificações:** UI01–UI12 — painel, lista, pesquisa, filtros, cadastro, persistência real após recarga, edição, conclusão, exclusão, exportação, ausência de erros JS e responsividade móvel.

**Arquivos de execução:** [resultado-testes-node.txt](resultado-testes-node.txt), [evidencias-testes-ui.txt](evidencias-testes-ui.txt).

*Os resultados são automatizados e não substituem a conferência final no computador do aluno.*
