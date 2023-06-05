# MyStore - Back-end

Este projeto é responsável por fornecer uma API RESTful para simular um sistema de estoque de produtos. É permitido realizar operações como listar, criar, atualizar e excluir produtos. Foi criado com a versão 4.2.1 do [Django](https://www.djangoproject.com/) sendo hospedado no servidor da [Heroku](https://heroku.com). A aplicação [Angular](https://github.com/angular/angular-cli) base encontra-se no domínio [https://mystore-vercel.vercel.app/](https://mystore-fe.vercel.app/)


## Requisitos básicos
- Python 3.9

## Instalação de dependências de desenvolvimento
Execute no terminal na pasta fonte do projeto:
```bash
pip install -r requirements.txt
```

## Configuração de Banco de dados local - SQLite3
Execute no terminal:
```bash
python manage.py makemigrations
```

Após bem-sucedido:
```bash
python manage.py migrate
```

## Servidor de desenvolvimento
Execute no terminal:
```bash
python manage.py runserver
```

## Endpoints da API
A API fornece os seguintes endpoints:

- Listar todos os produtos
  - URL: `/produtos/`
  - Método: **GET**
  - Descrição: Retorna uma lista de todos os produtos.

- Criar um novo produto
  - URL: `/produtos/`
  - Método: **POST**
  - Descrição: Cria um novo produto.

- Obter detalhes de um produto específico
  - URL: `/produtos/{id}/`
  - Método: **GET**
  - Descrição: Retorna os detalhes de um produto específico.

- Atualizar um produto específico
  - URL: `/produtos/{id}/`
  - Método: **PUT**
  - Descrição: Atualiza um produto específico.

- Atualizar parcialmente um produto específico
  - URL: `/produtos/{id}/`
  - Método: **PATCH**
  - Descrição: Atualiza parcialmente um produto específico.

- Excluir um produto específico
  - URL: `/produtos/{id}/`
  - Método: **DELETE**
  - Descrição: Exclui um produto específico.

- Formato JSON - GET/PUT/PATCH
  ```bash
  {
    "name": "Nome do Produto",
    "price": 10,
    "category": "Categoria do Produto"
  }
  ```

## Documentação oficial
Para mais informações sobre o Django e o Django REST framework, consulte a documentação oficial:

- Django
- Django REST framework
