# 📝 Django Blog

Projeto desenvolvido para a disciplina **Aplicações para Internet - UDF** - 1/2025.

## 🎓 Sobre o Projeto
Este projeto tem como objetivo explorar o **Django Models**, criando um sistema de blog que respeite as especificações solicitadas pelo professor.

## 🎯 Objetivo 
Criar um **blog**, onde usuários possam:
- 🔹 Publicar posts e categorias
- 🔹 Adicionar comentários
- 🔹 Enviar sugestões de novos posts
- 🔹 Interagir com avaliações e reações
- 🔹 Gerenciar conteúdo pelo **Django Admin**


## 👨‍🏫 Alunos
- Ana Carolina Barbosa de Souza - 27649865
- Fernando Rodrigues Leite Soares - 27727424
- Marcus Vinicius Portela da Costa - 27562689

## 🔧 Tecnologias Utilizadas
- Python 3.12
- Django 5.2
- SQLite/PostgreSQL
- HTML/CSS (para estilização)


## 📌 Especificações do Projeto
O código deve conter:
- ✅ **3 Relações** (_ForeignKey_, _ManyToMany_, _OneToOne_)
- ✅ **6 Models** (representando entidades do blog)
- ✅ **6 Meta Classes** (configuração do comportamento dos modelos)
- ✅ **5 Campos por Model** (definições como `CharField`, `TextField`, etc.)
- ✅ **6 Properties** (para atributos calculados)

---

## 📂 Estrutura do Projeto
```bash
django_blog/
│── blog/
│   ├── models.py       # Definição das models
│   ├── views.py        # Lógica das páginas
│   ├── urls.py         # Rotas do projeto
│   ├── templates/      # HTML dos templates
│   ├── static/         # Arquivos CSS/JS/imagens
│   ├── forms.py        # Definição dos formulários
│   ├── admin.py        # Configuração do Django Admin
```

---

## 🚀 Comandos Essenciais
### ▶️ **Configuração do Banco de Dados**
```bash
python manage.py makemigrations  # Criação das migrações
python manage.py migrate         # Aplicação das migrações
```

### ▶️ **Executar o Servidor**
```bash
python manage.py runserver  # Iniciar servidor local
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
