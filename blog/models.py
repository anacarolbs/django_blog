from django.db import models
from django.contrib.auth.models import User

# Model de Categorias
class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    #corrigir o nome de categorys para categories
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]
    #corrigir o nome do item para o que foi cadastrado 
    #Just like with common Python classes, you can add a .__str()__ method to model classes to provide a better string representation of your objects. For categories, you want to display the name. For posts, you want the title. For comments, show the name of the commenter and the post that they’re commenting on.
    def __str__(self):
        return self.name

    @property
    def post_count(self):
        return self.posts.count()

# Model de Posts
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts") #relacionamento entre post e categories 

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "Posts"
    #corrigir o nome do item para o que foi cadastrado 
    def __str__(self):
        return self.title

    @property
    def comment_count(self):
        return self.comments.count()

# Model de Comentários
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments") #relacionamento entre post e comentarios: many-to-one relationship (muitos comentarios podem estar em UM post, mas nao pode ter o mesmo comentario em varios posts)
#ai deletar um post, vc deleta os comentarios tambem
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]
        verbose_name_plural = "Comments"
    #corrigir o nome do item para o que foi cadastrado 
    def __str__(self):
        return f"{self.author} on '{self.post.title}'"

    @property
    def short_body(self):
        return self.body[:100] + "..." if len(self.body) > 100 else self.body

# Model de Reações (curtidas ou interações)
class Reaction(models.Model):
    REACTION_CHOICES = [
        ('like', 'Like'),
        ('love', 'Love'),
        ('haha', 'Haha'),
        ('wow', 'Wow'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reactions")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="reactions")
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Reactions"
        unique_together = ("user", "post")

    def __str__(self):
        return f"{self.user.username} reacted {self.reaction_type} on '{self.post.title}'"

    @property
    def reaction_summary(self):
        return f"{self.reaction_type} by {self.user.username}"

# Model de Pontuação de Post (PostRating)
class PostRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Notas de 1 a 5
    review = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "Post Ratings"
        unique_together = ("user", "post")

    def __str__(self):
        return f"Avaliação de {self.user.username} - {self.post.title}: {self.rating} estrelas"

    @property
    def rating_summary(self):
        return f"{self.rating} estrelas - {self.user.username}"

# Model de Histórico de Edição (EditHistory)
class EditHistory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="edit_history")
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    previous_content = models.TextField()
    edited_on = models.DateTimeField(auto_now_add=True)
    change_summary = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-edited_on"]
        verbose_name_plural = "Edit History"

    def __str__(self):
        return f"Edição de {self.edited_by.username} em {self.post.title}"

    @property
    def edit_summary(self):
        return f"Editado por {self.edited_by.username} em {self.edited_on.strftime('%d/%m/%Y %H:%M')}"



