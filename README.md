# QuestGameList
Trabalho de Gerenciamento e Configuração de dependência e DevOps Tools

---

# 🎮 Sistema de registros de jogos

---

## 🎯 Objetivo do site

### _Inspirado no site backlogg, nosso site tem como objetivo_ <br> 
### 1. _Registrar jogos que já jogou, está jogando ou quer jogar_ <br>
### 2. _Criar uma “backlog” (lista de jogos pendentes)_ <br>
### 3. _Avaliar jogos (com notas) e escrever reviews_ <br>
### 4. _Acompanhar progresso (tempo, datas, sessões)_
### 5. _Criar listas personalizadas (ex: “melhores RPGs”)_
### 6. _Seguir amigos e ver o que eles estão jogando_


---

## 📝 Requisitos Funcionais 

### Como requisitos funcionais, nosso projeto apresenta...

<details>
<summary><b>1. Gestão de Biblioteca & Backlog</b> (Clique para expandir)</summary>

* RF01 - Catálogo de Jogos: O usuário deve ser capaz de buscar jogos em uma base de dados global (via API IGDB/RAWG). 

* RF02 - Estados de Jogo: Possibilidade de marcar jogos como Jogado, Jogando, Quero Jogar ou Abandonado.

* RF03 - Filtros de Busca: Filtrar jogos por gênero, plataforma, ano de lançamento e avaliação.

* RF04 - Importação de Dados: Permitir que o usuário importe sua biblioteca de outras plataformas (ex: Steam).

</details>

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
│
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
```
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
     branches: [ "main", "principal" ]
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
