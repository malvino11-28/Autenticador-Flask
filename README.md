# Flask User Auth API

Este é um projeto simples de autenticação de usuários utilizando Flask e MySQL. O objetivo principal é a prática de desenvolvimento de APIs com Flask, incluindo funcionalidades básicas de cadastro, login e dashboard. O foco do projeto está no backend, portanto o frontend (HTML) é propositalmente simples.

## Funcionalidades

- Cadastro de usuários com senha criptografada (bcrypt)
- Login de usuários com verificação de senha
- Sessão de usuário e dashboard simples
- Logout de sessão
- Exibição de tabelas existentes no banco de dados

## Tecnologias utilizadas

- Python
- Flask
- MySQL
- bcrypt
- dotenv

## Deploy

Acesse o site aqui: [https://autenticador-flask-production.up.railway.app/cadastro]

## Estrutura do Projeto

```
flask-auth-app/
│
└── templates/           # Templates HTML
    ├── login.html       # Formulário de login
    └── registerPage.html# Formulário de cadastro
│
├── app.py               # Rota principal, cadastro e getTables
├── login.py             # Blueprint de login, dashboard e logout
├── requirements.txt     # Dependências do Python
├── schema.sql           # Script SQL para criar banco e tabela
├── .gitignore           # Arquivos ignorados pelo Git
├── .env                 # Variáveis de ambiente (não enviado ao repositório)

```

## Configuração do ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=dbdoll
FLASK_SECRET=segredo_super_secreto
```

## Banco de Dados

Para configurar o banco de dados, execute o conteúdo do arquivo `schema.sql` no seu MySQL.

```bash
mysql -u root -p < schema.sql
```

## Rodando a aplicação

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o servidor:

```bash
python app.py
```

Acesse via: `http://127.0.0.1:5000`

## Rotas principais

| Método | Rota       | Descrição                 |
| ------ | ---------- | ------------------------- |
| GET    | /login     | Página de login           |
| POST   | /login     | Processa login            |
| GET    | /cadastro  | Página de cadastro        |
| POST   | /cadastro  | Processa cadastro         |
| GET    | /dashboard | Página do usuário logado  |
| GET    | /logout    | Logout do usuário         |
| GET    | /getTables | Lista as tabelas do banco |

## Notas

- Este projeto é destinado ao estudo de backend com Flask. O frontend é simples pois não é o foco.
- A API pode ser expandida para incluir mais funcionalidades como reset de senha, implementar testes automatizados, integração com APIs externas ou conexão com frontend SPA (React, Vue etc).

## Autor

Feito como parte de prática de desenvolvimento com Flask e MySQL.
