<<<<<<< HEAD
# QuestGameList
Trabalho de Gerenciamento e Configuração de dependência e DevOps Tools

---

# 🎮 Sistema de registros de jogos

---
## 🎯 Objetivo do site

### _Inspirado no site backlogg, nosso site tem como objetivo_ <br> 
### 2. _Criar uma “backlog” (lista de jogos pendentes)_ <br>
### 3. _Avaliar jogos (com notas) e escrever reviews_ <br>
### 4. _Acompanhar progresso (tempo, datas, sessões)_
### 5. _Criar listas personalizadas (ex: “melhores RPGs”)_
### 6. _Seguir amigos e ver o que eles estão jogando_


---

## 📝 Requisitos Funcionais 


<details>
<summary><b>1. Gestão de Biblioteca & Backlog</b> (Clique para expandir)</summary>

* RF01 - Catálogo de Jogos: O usuário deve ser capaz de buscar jogos em uma base de dados global (via API IGDB/RAWG). 

* RF02 - Estados de Jogo: Possibilidade de marcar jogos como Jogado, Jogando, Quero Jogar ou Abandonado.

* RF03 - Filtros de Busca: Filtrar jogos por gênero, plataforma, ano de lançamento e avaliação.

* RF04 - Importação de Dados: Permitir que o usuário importe sua biblioteca de outras plataformas (ex: Steam).


<details>
<summary><b>2. Avaliações e Social</b> (Clique para expandir)</summary>

* RF05 - Sistema de Reviews: Escrita de análises críticas com suporte a alertas de spoiler.

* RF06 - Notas Numéricas: Atribuição de notas (0 a 10) para cada título finalizado.

* RF07 - Listas Personalizadas: Criação de coleções temáticas (ex: "Top 10 RPGs").

* RF08 - Rede Social: Seguir outros usuários, curtir reviews e visualizar o feed de atividades de amigos.
</details>

<details>
<summary><b>3. Progresso e Perfil</b> (Clique para expandir)</summary>

* RF09 - Contador de Horas: Registro manual ou automático do tempo investido em cada jogo.

* RF10 - Histórico de Sessões: Calendário mostrando quando o usuário iniciou e terminou cada título.

* RF11 - Estatísticas de Perfil: Gráficos automáticos exibindo gêneros mais jogados e tempo total de jogo.
</details>

<details>
<summary><b>4. Social e Interação</b> (Clique para expandir)</summary>

* RF12 - Sistema de Seguidores: Seguir perfis para acompanhar atualizações.

* RF13 - Feed de Atividade: Linha do tempo com as últimas ações dos amigos..

* RF14 - Interação: Curtir e comentar em reviews e listas.

</details>

<details>
<summary><b>5. Gerenciamento de Perfil</b> (Clique para expandir)</summary>

* RF15 - Autenticação: Cadastro e login seguro.

* RF16 - Personalização: Edição de avatar, bio e banners.

* RF17 - Dashboard: Visualização de estatísticas e gráficos de progresso.

</details>


---

## ⚙️ Requisitos não funcionais

<details>
  <summary><h3>Os requisitos não funcionais que nosso projeto apresenta são... (Clique para expandir)</h3></summary>
  
  * RNF01 - O sistema deve possuir interface simples e intuitiva.
    
  * RNF02 - O sistema deve possuir tempo de resposta rápido.
    
  * RNF03 - O sistema deve garantir segurança no login do usuário.
    
  * RNF04 - O sistema deve ser acessível em navegadores web modernos.
  
</details>
---

## 🤖 Tecnologias Usadas
<details>
  <summary><h3>As tecnologis que usamos... (Clique para expandir)</h3></summary>

  * Canva
  * HTML/CSS
  * Javascript
  * Node.js
  * GitHub
  * CI/CD
  * ChatGPT

</details>
---

## 📝 Descrição do Problema que o Projeto Pretende Resolver 

### _Esse "Backlog" tem como objetivo solucionar alguns problemas como:_ <br>
### 1. _Dificuldade em lembrar jogos finalizados, abandonados ou em andamento (Jogadores não possuem um local centralizado para acompanhar seu histórico.)_
### 2. _Dificuldade em descobrir novos jogos (Encontrar bons jogos pode ser confuso devido à grande quantidade disponível.)_
### 3. _Ausência de avaliações organizadas (Não há um espaço estruturado para registrar opiniões sobre jogos)_
### 4. _Falta de registro pessoal (Jogadores não possuem um local centralizado para acompanhar seu histórico.)_


---

## 📦 Estrutura do repositório
### Árvore do site no repositório
```
quest-game-list/
│
├── docs/
│   ├── arquitetura.md
│   ├── requisitos.md
│   ├── diagramas/
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── profile.html
│   │
│   ├── assets/
│   │   ├── images/
│   │   ├── icons/
│   │   └── fonts/
│   │
│   ├── css/
│   │   ├── main.css
│   │   ├── layout.css
│   │   ├── components.css
│   │   └── pages/
│   │       ├── home.css
│   │       ├── login.css
│   │       ├── dashboard.css
│   │       └── profile.css
│   │
│   └── js/
│       ├── app.js
│       ├── auth.js
│       ├── games.js
│       └── ui.js
│
├── backend/
│   ├── app/
│   │   ├── controllers/
│   │   ├── services/
│   │   ├── models/
│   │   └── routes/
│   │
│   ├── config/
│   │   └── database.py
│   │
│   └── main.py
│
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   └── migrations/
│
├── devops/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── nginx.conf
│   └── pipeline.yml
│
├── tests/
│   ├── frontend/
│   └── backend/
│
├── .gitignore
├── README.md
└── package.json
```
---

## 🧠 Explicação do workflow (ci.yml)
```
Nosso caso, o workflow é o arquivo ci.yml, onde configuramos as etapas automáticas que o GitHub vai executar sempre que houver um push no projeto.

-> Explicação mais detalhada

O workflow organiza todo o processo de integração contínua, definindo eventos (como push), tarefas (jobs) e os passos (steps) que serão executados automaticamente.

Workflow é tipo um roteiro automático do que o sistema deve fazer.
O workflow foi usado para automatizar tarefas simples como exibir mensagens e verificar os arquivos, garantindo que o projeto esteja organizado.

Workflow → o arquivo com as regras (ci.yml)
Pipeline → o processo rodando
---

## 🔄 Explicação do pipeline
O que é o pipeline?
O pipeline é um processo automático que roda quando você faz um push no GitHub, ou seja, sempre que alguém da equipe subir código, o GitHub automaticamente executa algumas tarefas.
O que o pipeline precisa entregar?
 Pipeline precisa ter pelo menos 3 coisas:
1.	 Mostrar uma mensagem no console
2.	 Executar algum script do projeto
3.	 Listar arquivos ou validar algo
---

## 🌀 Fluxo de execução do pipeline

## Como foi aplicado:
```
 Criamos um arquivo no repositório chamado (.github/workflows/ci.yml). Nosso pipeline foi configurado com GitHub Actions e é executado automaticamente a cada push no repositório.
on:
   push:
jobs:
      test:
      runs-on: ubuntu-latest
      steps:
      -name: Clonar repositório
      uses: actions/checkout@v3
      - name: Mostrar mensagem
      run: echo "Pipeline funcionando com sucesso "
      - name: Listar arquivos
       run: ls -la
       - name: Finalizar
       run: echo "Tudo certo!"

Ele realiza três etapas principais:
Exibe uma mensagem confirmando execução
Lista os arquivos do projeto
Simula a execução do sistema
```
=======
# quest-game-list# 🎮 GameBacklog - Sistema de Gestão de Jogos
Evolução da Infraestrutura e Gerência de Configuração (Unidade 2).

## 🚀 Parte 5 - Kubernetes Simplificado

* **O que é Kubernetes:** É um orquestrador de containers de código aberto que automatiza a implantação, o dimensionamento e o gerenciamento de aplicações em containers.
* **O que é Pod:** É a menor unidade básica de execução no Kubernetes. Um Pod representa um único processo em execução no cluster e pode conter um ou mais containers compartilhando recursos.
* **O que é Service:** É uma abstração que define uma política de acesso e um endereço de rede estável (IP/Porta) para permitir que os usuários ou outros serviços acessem os Pods, distribuindo a carga de tráfego entre eles.
* **Como ajudaria o sistema:** Ele eliminaria quedas manuais do sistema de jogos. Se o volume de usuários buscando jogos por API (RF01) ou atualizando perfis aumentar drasticamente, o Kubernetes cria novas réplicas de forma automática.

---

## 📈 Parte 7 - Escalabilidade

1. **Como o Kubernetes ajudaria se muitos usuários acessassem o sistema?**
   Através do *Horizontal Pod Autoscaler (HPA)*, ele identificaria o aumento de consumo de CPU/Memória e criaria novos Pods (réplicas) do sistema de jogos para absorver a carga, distribuindo o tráfego de maneira uniforme.
   Significa rodar cópias idênticas do container da aplicação simultaneamente. No nosso `deployment.yaml`, definimos 3 réplicas, ou seja, o sistema aguenta 3 vezes mais requisições simultâneas de usuários mexendo na rede social de games.
3. **O que poderia acontecer se um Pod falhasse?**
   O mecanismo de autocura (*Self-healing*) do Kubernetes detectaria imediatamente a falha do Pod, destruiria a instância corrompida e subiria um novo Pod saudável no lugar em questão de segundos, sem que o usuário final percebesse a instabilidade.

---

## ⚙️ Parte 8 - Gerência de Configuração do Projeto

### 8.1 Itens de Configuração do Projeto (IC)
* **Código-Fonte (`app/main.py`):** Controlado via Git para registrar novas funcionalidades como o feed de atividades e o contador de horas.
* **Dockerfile:** Precisa ser controlado porque define o ambiente exato de execução da aplicação. Qualquer mudança incorreta quebra a imagem.
* **deployment.yaml:** Controlado para garantir que os limites de recursos e réplicas em produção correspondam à arquitetura validada.
* **Requirements.txt:** Controla as versões exatas do FastAPI e Uvicorn para evitar que atualizações externas de terceiros quebrem o código.

### 8.2 Baseline do Projeto
* **Nome da Baseline:** `Baseline_Unidade_2`
* **Versão Associada:** `v2.0.0`
* **Arquivos Integrantes:** `app/main.py`, `Dockerfile`, `deployment.yaml`, `app/requirements.txt`, `README.md`.
* **Motivo da Estabilidade:** Esta versão passou com sucesso pelos testes de containerização locais no GitHub Codespaces, possui a API base de rotas funcionais mapeadas e documentação completa.

### 8.3 Estratégia de Versionamento
Adotamos o padrão **Semantic Versioning (MAJOR.MINOR.PATCH)**:
* `v1.0.0`: Entrega inicial da aplicação web básica da Primeira Unidade.
* `v2.0.0`: Segunda Unidade: Containerização com Docker, escrita de manifesto Kubernetes e estruturação de gerência de configuração.
* `v2.0.1`: Correções rápidas de bugs e patches de segurança.

### 8.4 Controle de Mudanças (Histórico)
* **Mudança 1:** Migração de arquitetura legada para estrutura em Containers (Docker).
  * **Itens impactados:** Raiz do projeto, adição do `Dockerfile`.
  * **Motivo:** Garantir portabilidade em qualquer ambiente.
  * **Status:** Concluído.
* **Mudança 2:** Implementação das rotas backend de CRUD de Jogos (RF02 e RF03).
  * **Itens impactados:** `app/main.py`.
  * **Motivo:** Permitir a filtragem e troca de estado dos jogos via API.
  * **Status:** Concluído.
* **Mudança 3:** Adicionado arquivo de provisionamento Kubernetes.
  * **Itens impactados:** Criação do arquivo `deployment.yaml`.
  * **Motivo:** Atender ao requisito de escalabilidade para picos de tráfego.
  * **Status:** Concluído.

### 8.5 Solicitação de Mudança (Fictícia)
* **Título da mudança:** Implementação de Integração Real com API RAWG/IGDB (RF01).
* **Descrição:** Substituir o banco simulado na memória por requisições HTTP reais de catálogo de jogos.
* **Motivo:** O usuário precisa de uma base global atualizada e real de títulos.
* **Itens impactados:** `app/main.py`, `app/requirements.txt` (Adição da biblioteca `httpx`).
* **Riscos envolvidos:** Lentidão em chamadas externas se a API parceira cair (afeta RNF02).
* **Prioridade:** Média.
* **Necessidade de testes:** Sim, testes de integração e tratamento de timeout.
* **Decisão:** Aprovado para a Unidade 3.

### 8.6 Auditoria de Configuração
| Item verificado | Conforme? | Observação |
| :--- | :---: | :--- |
| README atualizado | Sim | Seções de gerência de configuração devidamente detalhadas. |
| Dockerfile presente | Sim | Na raiz do projeto utilizando imagem alpine/slim. |
| deployment.yaml presente | Sim | Configurado com 3 réplicas e limites de recursos. |
| Imagem Docker versionada | Sim | Tagged como `:v2` no Docker Hub. |
| Baseline definida | Sim | Marcada como v2.0.0 estável. |

### 8.7 Gerência de Dependências
1. **Quais dependências o projeto utiliza?** Python 3.10-slim, FastAPI, Uvicorn e Pydantic.
2. **Onde estão registradas?** No arquivo `app/requirements.txt` e no manifesto do `Dockerfile`.
3. **Qual risco se atualizadas sem teste?** Uma alteração de sintaxe na biblioteca FastAPI ou Pydantic pode quebrar a inicialização do container (violando o RNF02 de disponibilidade).
4. **Como controlar a atualização?** Fixando versões exatas no `requirements.txt` (ex: `fastapi==0.110.0`) e utilizando um pipeline de CI para rodar testes automatizados antes de aprovar qualquer Pull Request de atualização.
>>>>>>> 1622e9d (Prepara projeto FastAPI/Docker para compartilhamento)
