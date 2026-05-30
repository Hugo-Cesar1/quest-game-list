# QuestGameList

Trabalho de Gerenciamento e Configuracao de Dependencias e DevOps Tools.

## Sistema

Aplicacao web com FastAPI e paginas HTML/CSS para registro e organizacao de jogos.

## Colaboracao

O fluxo oficial de contribuicao usa branch + Pull Request.

- Guia completo: [CONTRIBUTING.md](CONTRIBUTING.md)
- Template de PR: [.github/pull_request_template.md](.github/pull_request_template.md)

Resumo rapido:

1. Atualize a branch main.
2. Crie uma branch de trabalho (`feat/*`, `fix/*`, `docs/*`, `chore/*`).
3. Abra Pull Request para main.
4. Aguarde CI verde e revisao antes do merge.

## Estrutura principal

```text
quest-game-list/
├── app/
│   ├── main.py
│   ├── requirements.txt
│   ├── static/
│   └── templates/
├── deployment.yaml
├── Dockerfile
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   └── pull_request_template.md
└── CONTRIBUTING.md
```

## Executar localmente

```bash
pip install -r app/requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Depois, abra:

- http://localhost:8000/

## Docker

```bash
docker build -t quest-game-list:local .
docker run --rm -p 8000:8000 quest-game-list:local
```

## Kubernetes

O arquivo [deployment.yaml](deployment.yaml) contem:

- 1 Deployment (3 replicas)
- 1 Service (ClusterIP)

Aplicacao:

```bash
kubectl apply -f deployment.yaml
```

## CI

Pipeline configurada em [.github/workflows/ci.yml](.github/workflows/ci.yml) para rodar em push/PR na main:

1. Setup Python
2. Instalacao de dependencias
3. Validacao de sintaxe Python
4. Validacao do manifesto Kubernetes
5. Smoke test da aplicacao FastAPI
