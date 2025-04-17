from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30) #tamanho máximo de 30 caracteres

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts") #relacionamento entre post e categories

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE) #relacionamento entre post e comentarios: many-to-one relationship (muitos comentarios podem estar em UM post, mas nao pode ter o mesmo comentario em varios posts)
#ai deletar um post, vc deleta os comentarios tambem




