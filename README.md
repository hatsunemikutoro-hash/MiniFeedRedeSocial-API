# MiniFeedRedeSocial-API

Um projeto pequeno e simples de feed social, feito com Flask, usando a API pública do JSONPlaceholder como base de dados de exemplo.

A ideia é bem leve: o backend busca posts de usuários, salva no banco e exibe uma interface simples no navegador.

## O que o projeto faz

- carrega posts da API do JSONPlaceholder
- salva os dados em um banco MySQL
- expõe uma rota para importar os posts
- renderiza uma página simples com HTML, CSS e JavaScript

## Tecnologias

- Python
- Flask
- MySQL Connector
- Requests
- HTML
- CSS
- JavaScript

## Estrutura do projeto

- `main.py` - aplicação Flask
- `templates/` - arquivos HTML
- `static/` - estilos e scripts do frontend

## Pré-requisitos

Antes de rodar o projeto, tenha instalado:

- Python 3
- MySQL local
- pip

## Configuração do banco

O projeto usa um banco chamado `posts_json` com uma tabela `posts`.

Exemplo de estrutura esperada:

```sql
CREATE DATABASE posts_json;

USE posts_json;

CREATE TABLE posts (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    body TEXT,
    postid INT
);
```

A conexão está configurada em `main.py` com:

```python
 db_config = {
     'host': 'localhost',
     'user': 'root',
     'password': 'root',
     'database': 'posts_json'
 }
```

Se o seu ambiente for diferente, ajuste esses valores.

## Instalação

```bash
pip install flask requests mysql-connector-python
```

## Como rodar

```bash
python main.py
```

Depois, abra no navegador:

```bash
http://localhost:5000
```

## Endpoints

### GET /

Página principal da aplicação.

### GET /import

Busca os posts do usuário 1 na API do JSONPlaceholder e salva no banco MySQL.

## Observações

Este projeto é mais didático do que complexo, então ele funciona como uma base simples para aprender integração entre backend, banco de dados e frontend.

Se quiser, pode evoluir com:

- listagem mais bonita de posts
- comentários por post
- cadastro de novos posts
- filtros e busca
- autenticação simples

