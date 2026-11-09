# Testes e validação
O sistema foi validado na preparação do projeto em 09/11/2026 com **10 testes automatizados** e **12 verificações de interface**. O pacote original inclui scripts e logs detalhados.

| Caso | Funcionalidade | Procedimento | Esperado | Obtido | Situação |
|---|---|---|---|---|---|
| CT01 | Cadastro | Cadastrar uma tarefa válida | Registro aparece na lista | Registro criado e listado | Aprovado |
| CT02 | Consulta/filtro | Filtrar tarefas por status | Mostrar apenas itens correspondentes | Filtro aplicado | Aprovado |
| CT03 | Edição | Alterar uma tarefa | Dados atualizados | Dados atualizados | Aprovado |
| CT04 | Status | Concluir tarefa | Estatísticas/status atualizados | Status atualizado | Aprovado |
| CT05 | Exclusão | Remover tarefa após confirmar | Item removido | Item removido | Aprovado |
| CT06 | Validação | Submeter título vazio | Bloquear cadastro | Cadastro bloqueado | Aprovado |

**Limitação:** verificações da interface ocorreram em navegador automatizado com implementação de Storage em memória; testar manualmente em ambiente do aluno antes da entrega.
