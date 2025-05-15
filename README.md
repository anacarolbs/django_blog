# 📝 Django Blog

Projeto desenvolvido para a disciplina **Aplicações para Internet - UDF** - 1/2025.

## ✒️ Alunos
- Ana Carolina Barbosa de Souza - 27649865
- Fernando Rodrigues Leite Soares - 27727424
- Marcus Vinicius Portela da Costa - 27562689


## 🎓 Sobre o Projeto
Este projeto tem como objetivo explorar o **Django** e suas principais funcionalidades, criando um sistema de blog que respeite as especificações solicitadas pelo professor.

## 🎯 Objetivo 
Criar um **blog**, onde usuários possam:
- 🔹 Publicar posts e categorias
- 🔹 Adicionar comentários
- 🔹 Enviar sugestões de novos posts
- 🔹 Interagir com avaliações e reações
- 🔹 Gerenciar conteúdo pelo **Django Admin**


## 🔧 Tecnologias Utilizadas
- Python 3.12
- Django 5.2
- SQLite/PostgreSQL
- HTML/CSS (para estilização)
- Bootstrap 5


## 📌 Especificações do Projeto
### Módulo de Models
08/04 - Django Models e Databases  
15/04 - Django Forms e ModelForms  
O código deve conter:
- 3 Relações (_ForeignKey_, _ManyToMany_, _OneToOne_)
- 6 Models (representando entidades do blog)
- 6 Meta Classes (configuração do comportamento dos modelos)
- 5 Campos por Model (definições como `CharField`, `TextField`, etc.)
- 6 Properties (para atributos calculados)

### Módulo de Templates
22/04 - Django Template e Bootstrap  
29/04 - Crispy Forms e Weasy Print  
O código deve conter:
- 3 Templates
- 3 Forms 
- 3 Models
- 3 Formulários Estilizados 
- 2 Condicionais 
- 2 Loop: 1 For e 1 While 
- 3 Filtros 
- 2 Include 

### Módulo de Views
06/05 - Django Views e ModelViews  
13/05 - Django Class-Based Generic Views  
O código deve conter:
- 1 Classe Criar
- 1 Classe Editar 
- 1 Classe Detalhar
- 1 Classe Listar 
- 1 Classe Deletar 
- 1 Método Criar 
- 1 Método Editar
- 1 Método Detalhar 
- 1 Método Listar 
- 1 Método Deletar

### Módulo de API
20/05 - Django Rest Framework  
27/05 - FastAPI

---

## 📂 Estrutura do Projeto
```bash
django_blog/
├── blog/                         # Aplicativo principal do blog
│   ├── migrations/               # Arquivos de migração do banco de dados
│   ├── static/                   # Arquivos estáticos (CSS, JS, imagens)
│   ├── templates/                # Templates HTML do aplicativo
│   │   ├── blog/                 # Templates específicos do blog
│   │   │   ├── base.html         # Template base para herança
│   │   │   ├── index.html        # Página inicial do blog
│   │   │   ├── post_list.html    # Lista de posts
│   │   │   ├── post_detail.html  # Detalhes de um post
│   │   │   ├── post_form.html    # Formulário para criar/editar posts
│   │   │   ├── confirm_delete_post.html # Página de confirmação de exclusão
│   │   │   └── ...               # Outros templates
│   ├── templatetags/             # Filtros personalizados para templates
│   │   └── blog_filters.py       # Filtros personalizados do blog
│   ├── admin.py                  # Configuração do painel de administração
│   ├── apps.py                   # Configuração do aplicativo
│   ├── forms.py                  # Formulários do blog
│   ├── models.py                 # Modelos do banco de dados
│   ├── urls.py                   # Rotas do aplicativo
│   ├── views.py                  # Views do aplicativo
│   └── tests.py                  # Testes automatizados
├── personal_blog/                # Configurações do projeto Django
│   ├── settings.py               # Configurações globais do projeto
│   ├── urls.py                   # Rotas globais do projeto
│   ├── wsgi.py                   # Configuração do WSGI
│   └── asgi.py                   # Configuração do ASGI
├── manage.py                     # Script de gerenciamento do Django
├── db.sqlite3                    # Banco de dados SQLite (padrão)
└── README.md                     # Documentação do projeto
```

---

## 🚀 Comandos Essenciais
### ▶️ **Criar o diretório**
```bash
mkdir django-blog
$ cd django-blog
```
### ▶️ **Criar um ambiente virtual**
```bash
python -m venv venv
```
### ▶️ **Ativar o ambiente virtual**
```bash
source venv/bin/activate
```
### ▶️ **Instalar o django**
```bash
python -m pip install Django
```
### ▶️ **Criar o projeto**
```bash
django-admin startproject personal_blog 
``` 
### ▶️ **Criar e aplicar as migrações**
```bash
python manage.py makemigrations  # Criação das migrações
python manage.py migrate         # Aplicação das migrações
```
### ▶️ **Iniciar o servidor de desenvolvimento**
```bash
python manage.py runserver
```
### ▶️ **Acessar o localhost**
http://localhost:8000 
### ▶️ **Criar a aplicação**
```bash
python manage.py startapp blog
```
### ▶️ **Criar Superusuário**
```bash
python manage.py createsuperuser  # Acesso ao Django Admin
```
---

## 📚 Referências
- 📖 [Django Models](https://docs.djangoproject.com/en/5.1/topics/db/models/)
- 📖 [Model Reference](https://docs.djangoproject.com/en/5.1/ref/models/)
- 📖 [Queries no Django](https://docs.djangoproject.com/en/5.1/topics/db/queries/)
- 📖 [Exemplos Práticos](https://docs.djangoproject.com/en/5.1/topics/db/examples/)
- 📖 [Exemplo de Projeto](https://realpython.com/build-a-blog-from-scratch-django/)
- 📖 [Templates](https://docs.djangoproject.com/en/5.2/topics/templates/)
- 📖 [The Django template language](https://docs.djangoproject.com/en/5.2/ref/templates/language/)
- 📖 [Built-in template tags and filters](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/)
