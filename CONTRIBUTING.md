# Guia de Colaboracao

Este repositorio usa fluxo baseado em branch + Pull Request.

## Fluxo de trabalho

1. Atualize sua `main` local.
2. Crie uma branch para a tarefa.
3. Faça commits pequenos e claros.
4. Envie a branch para o remoto.
5. Abra Pull Request para `main`.
6. Aguarde CI verde e revisao.
7. Faça merge do PR.

## Padrao de branch

- `feat/nome-curto-da-feature`
- `fix/nome-curto-do-bug`
- `chore/nome-curto-da-tarefa`
- `docs/nome-curto-da-doc`

Exemplo:

`feat/tela-perfil`

## Padrao de commit

Preferencia por Conventional Commits:

- `feat: adiciona pagina de perfil`
- `fix: corrige rota de procurar`
- `docs: atualiza instrucoes de deploy`

## Regras para Pull Request

- O PR deve ter descricao do problema e da solucao.
- O PR deve listar como testar.
- O PR deve passar no workflow de CI.
- Pelo menos 1 aprovacao antes do merge.

## Comandos rapidos

```bash
git checkout main
git pull origin main
git checkout -b feat/minha-mudanca

# ...edite o codigo...

git add .
git commit -m "feat: minha mudanca"
git push -u origin feat/minha-mudanca
```