from django import forms
from .models import PostSuggestion

# Formulário para comentários
class CommentForm(forms.Form):
    # Campo para o nome do autor do comentário
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Seu Nome"}
        ),
    )
    # Campo para o e-mail do autor (opcional)
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Seu Email (opcional)"}
        ),
    )
    # Campo para o corpo do comentário
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Deixe um comentário!", "rows": 4}
        ),
        min_length=5  # Validação para evitar comentários muito curtos
    )

# Formulário para criação de enquetes
class PollForm(forms.Form):
    # Campo para a pergunta da enquete
    question = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite a pergunta da enquete"}),
        label="Pergunta",
    )
    # Campo para a primeira opção de resposta
    option_one = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Opção 1"}),
        label="Opção 1",
    )
    # Campo para a segunda opção de resposta
    option_two = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Opção 2"}),
        label="Opção 2",
    )
    # Campo para a terceira opção de resposta (opcional)
    option_three = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Opção 3 (opcional)"}),
        label="Opção 3",
    )

# Formulário para criação de posts no blog (crispy_forms)
class BlogPostForm(forms.Form):
    # Campo para o título do post
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o título do post"}),
        label="Título",
    )
    # Campo para o conteúdo do post
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Digite o conteúdo do post", "rows": 6}),
        label="Conteúdo",
    )
    # Campo para a categoria do post
    category = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite a categoria"}),
        label="Categoria",
    )
    # Campo para as tags do post (opcional)
    tags = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite as tags separadas por vírgula"}),
        label="Tags",
    ) 

# Formulário para sugestões de post (crispy_forms)
class PostSuggestionForm(forms.ModelForm):
    class Meta:
        model = PostSuggestion
        # Campos do modelo `PostSuggestion` que serão exibidos no formulário
        fields = ["title", "description"]
        labels = {
            "title": "Título",
            "description": "Descrição",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o título da sugestão"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Descreva sua sugestão", "rows": 4}),
        }

# Formulário para inscrição na newsletter (crispy_forms)
class NewsletterSignupForm(forms.Form):
    # Campo para o e-mail do usuário
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Digite seu e-mail"}),
        label="E-mail",
    )
# Formulário para registro de eventos (crispy_forms)
class EventRegistrationForm(forms.Form):
    # Campo para o nome do evento
    event_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome do Evento"}),
        label="Nome do Evento",
    )
    # Campo para a data do evento
    date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        label="Data do Evento",
    )
    # Campo para o local do evento
    location = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Local do Evento"}),
        label="Local",
    )
    # Campo para a descrição do evento
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Descrição do Evento", "rows": 4}),
        label="Descrição",
    )