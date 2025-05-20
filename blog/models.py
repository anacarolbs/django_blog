from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now 

# Model de Categorias
class Category(models.Model):
    # Nome da categoria, que deve ser único.
    name = models.CharField(max_length=30, unique=True)
    # Descrição opcional da categoria.
    description = models.TextField(blank=True, null=True)
    # Data de criação da categoria.
    created_on = models.DateTimeField(default=now)
    # Data da última atualização da categoria.
    updated_on = models.DateTimeField(auto_now=True)
    # Indica se a categoria está ativa.
    is_active = models.BooleanField(default=True)

    class Meta:
        # Configurações adicionais: nome plural e ordenação por nome.
        verbose_name_plural = "Categories"
        ordering = ["name"]
    #corrigir o nome do item para o que foi cadastrado 
    def __str__(self):
        return self.name

    # Propriedade que retorna o número de posts associados à categoria.
    @property
    def post_count(self):
        return self.posts.count()

# Model de Posts
class Post(models.Model):
    # Título do post.
    title = models.CharField(max_length=255)
    # Corpo do post.
    body = models.TextField()
    # Relacionamento com o autor (usuário). Se o autor for excluído, os posts também serão.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", default=1)  
    # Data de criação do post.
    created_on = models.DateTimeField(auto_now_add=True)
    # Data da última modificação do post.
    last_modified = models.DateTimeField(auto_now=True)
    # Relacionamento muitos-para-muitos com categorias.
    categories = models.ManyToManyField("Category", related_name="posts") #relacionamento entre post e categories 

 #Configurações adicionais: nome plural e ordenação por data de criação (mais recente primeiro).
    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "Posts"
    #corrigir o nome do item para o que foi cadastrado 
    def __str__(self):
        return self.title

# Propriedade que retorna o número de comentários associados ao post.
    @property
    def comment_count(self):
        return self.comments.count()

# Model de Comentários
class Comment(models.Model):
    # Nome do autor do comentário.
    author = models.CharField(max_length=60, verbose_name="Autor")
    # Corpo do comentário.
    body = models.TextField(verbose_name="Comentário")
    # Data de criação do comentário.
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    # Relacionamento com o post. Se o post for excluído, os comentários também serão.
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments", verbose_name="Post") #relacionamento entre post e comentarios: many-to-one relationship (muitos comentarios podem estar em UM post, mas nao pode ter o mesmo comentario em varios posts)
    # Indica se o comentário foi aprovado.
    is_approved = models.BooleanField(default=False, verbose_name="Aprovado")

# Configurações adicionais: nome plural e ordenação por data de criação.
    class Meta:
        ordering = ["created_on"]
        verbose_name = "Comentário"
        verbose_name_plural = "Comments"
    #corrigir o nome do item para o que foi cadastrado 
    def __str__(self):
        return f"{self.author} on '{self.post.title}'"

# Propriedade que retorna uma versão truncada do corpo do comentário.
    @property
    def short_body(self):
        return self.body[:100] + "..." if len(self.body) > 100 else self.body

# Model de Reações (curtidas ou interações)
class Reaction(models.Model):
    # Tipos de reações disponíveis.
    REACTION_CHOICES = [
        ('like', '👍'),
        ('love', '❤️'),
        ('haha', '😂'),
        ('wow', '😲'),
        ('sad', '😢'),
        ('angry', '😡'),
    ]
    # Relacionamento com o usuário que reagiu.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reactions")
    # Relacionamento com o post reagido.
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="reactions")
    # Tipo de reação.
    reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)
    # Data de criação da reação.
    created_on = models.DateTimeField(auto_now_add=True)
    # Data da última atualização da reação.
    updated_on = models.DateTimeField(auto_now=True)

# Configurações adicionais: nome plural e restrição de unicidade (um usuário pode reagir apenas uma vez a um post).
    class Meta:
        verbose_name_plural = "Reactions"
        unique_together = ("user", "post")

#corrigir o nome do item para o que foi cadastrado 
    def __str__(self):
        return f"{self.user.username} reagiu {self.reaction_type} em '{self.post.title}'"

    @property
    # Retorna uma string formatada com o tipo de reação e o nome do usuário que reagiu
    def reaction_summary(self):
        return f"{self.reaction_type} por {self.user.username}"

# Model de Avaliações de Post (PostRating)
class PostRating(models.Model):
    # Relacionamento com o usuário que avaliou.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    # Relacionamento com o post avaliado.
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="ratings")
    # Nota de 1 a 5.
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Notas de 1 a 5
    # Comentário opcional sobre a avaliação.
    review = models.TextField(blank=True, null=True)
    # Data de criação da avaliação.
    created_on = models.DateTimeField(auto_now_add=True)
    # Data da última atualização da avaliação.
    updated_on = models.DateTimeField(auto_now=True)

# Configurações adicionais: nome plural, ordenação por data de criação e restrição de unicidade.
    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "Post Ratings"
        unique_together = ("user", "post")

    def __str__(self):
        return f"Avaliação de {self.user.username} - {self.post.title}: {self.rating} estrelas"

    @property
    def rating_summary(self):
        return f"{self.rating} estrelas - {self.user.username}"

# Model de Sugestões de Post (PostSuggestion)
class PostSuggestion(models.Model):
    # Relacionamento com o usuário que sugeriu (opcional).
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Usuário opcional
    # Título da sugestão.
    title = models.CharField(max_length=255)
    # Descrição da sugestão.
    description = models.TextField()
    # Data de criação da sugestão.
    created_on = models.DateTimeField(auto_now_add=True)
    # Status da sugestão (pendente, aprovado ou rejeitado).
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "⏳ Pendente"),
            ("approved", "✅ Aprovado"),
            ("rejected", "❌ Rejeitado"),
        ],
        default="pending",
    )

# Configurações adicionais: nome plural e ordenação por data de criação.
    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "Post Suggestions"

    def __str__(self):
        return f"Sugestão: {self.title} ({self.get_status_display()})"

# A PARTIR DAQUI MODELS DA SEGUNDA ENTREGA 

# Model de Eventos
class Event(models.Model):
    # Nome do evento.
    event_name = models.CharField(max_length=200)
    # Data do evento.
    date = models.DateField()
    # Local do evento.
    location = models.CharField(max_length=200)
    # Descrição do evento.
    description = models.TextField()

    def __str__(self):
        return self.event_name

# Model de Enquetes
class Poll(models.Model):
    # Pergunta da enquete.
    question = models.CharField(max_length=200)
    # Primeira opção de resposta.
    option_one = models.CharField(max_length=100)
    # Segunda opção de resposta.
    option_two = models.CharField(max_length=100)
    # Terceira opção de resposta (opcional).
    option_three = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.question

# Model de Enquetes com Votos
class VotePoll(models.Model):
    # Pergunta da enquete.
    question = models.CharField(max_length=200)
    # Primeira opção de resposta.
    option_one = models.CharField(max_length=100)
    # Segunda opção de resposta.
    option_two = models.CharField(max_length=100)
    # Terceira opção de resposta (opcional).
    option_three = models.CharField(max_length=100, blank=True, null=True)
    # Número de votos para a primeira opção.
    votes_option_one = models.IntegerField(default=0)
    # Número de votos para a primeira opção.
    votes_option_two = models.IntegerField(default=0)
    # Número de votos para a terceira opção.
    votes_option_three = models.IntegerField(default=0)

    def __str__(self):
        return self.question

# Model de Posts do Blog
class BlogPost(models.Model):
    # Título do post.
    title = models.CharField(max_length=200)
    # Conteúdo do post.
    content = models.TextField()
    # Categoria do post.
    category = models.CharField(max_length=100)
    # Tags do post (opcional).
    tags = models.CharField(max_length=200, blank=True, null=True)
    # Data de criação do post.
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title