from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30) #tamanho máximo de 30 caracteres

    #corrigir o nome de categorys para categories
    class Meta:
        verbose_name_plural = "categories"

    #corrigir o nome do item para o que foi cadastrado 
    #Just like with common Python classes, you can add a .__str()__ method to model classes to provide a better string representation of your objects. For categories, you want to display the name. For posts, you want the title. For comments, show the name of the commenter and the post that they’re commenting on.
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts") #relacionamento entre post e categories
    
    #corrigir o nome do item para o que foi cadastrado 
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE) #relacionamento entre post e comentarios: many-to-one relationship (muitos comentarios podem estar em UM post, mas nao pode ter o mesmo comentario em varios posts)
#ai deletar um post, vc deleta os comentarios tambem

    #corrigir o nome do item para o que foi cadastrado 
    def __str__(self):
        return f"{self.author} on '{self.post}'"




