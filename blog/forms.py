from django import forms
from .models import PostSuggestion

#form
class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Seu Nome"}
        ),
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Seu Email (opcional)"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Deixe um comentário!", "rows": 4}
        ),
        min_length=5  # Adicionando validação para evitar comentários muito curtos
    )

#form
class PollForm(forms.Form):
    question = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite a pergunta da enquete"}),
        label="Pergunta",
    )
    option_one = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Opção 1"}),
        label="Opção 1",
    )
    option_two = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Opção 2"}),
        label="Opção 2",
    )
    option_three = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Opção 3 (opcional)"}),
        label="Opção 3",
    )

#form 
class BlogPostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o título do post"}),
        label="Título",
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Digite o conteúdo do post", "rows": 6}),
        label="Conteúdo",
    )
    category = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite a categoria"}),
        label="Categoria",
    )
    tags = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite as tags separadas por vírgula"}),
        label="Tags",
    ) 

#crispy_forms
class PostSuggestionForm(forms.ModelForm):
    class Meta:
        model = PostSuggestion
        fields = ["title", "description"]
        labels = {
            "title": "Título",
            "description": "Descrição",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite o título da sugestão"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Descreva sua sugestão", "rows": 4}),
        }

#crispy_forms
class NewsletterSignupForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Digite seu e-mail"}),
        label="E-mail",
    )
#crispy_forms
class EventRegistrationForm(forms.Form):
    event_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome do Evento"}),
        label="Nome do Evento",
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        label="Data do Evento",
    )
    location = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Local do Evento"}),
        label="Local",
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Descrição do Evento", "rows": 4}),
        label="Descrição",
    )