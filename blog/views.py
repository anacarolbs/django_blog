from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Comment, Category, Reaction, PostRating, PostSuggestion, VotePoll, Event
from django.http import HttpResponseRedirect
from blog.forms import CommentForm, PollForm, BlogPostForm, PostSuggestionForm, NewsletterSignupForm, EventRegistrationForm
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from blog.forms import CommentModelForm
from .serializers import PostSerializer, CategorySerializer, CommentSerializer
from rest_framework import viewsets

# Página inicial do blog
def blog_index(request):
    # Obtém todos os posts ordenados pela data de criação (mais recentes primeiro).
    posts = Post.objects.all().order_by("-created_on")
    # Limita a exibição aos 30 primeiros posts.
    recent_posts = []
    i = 0
    while i < len(posts) and i < 30:  
        recent_posts.append(posts[i])
        i += 1

    context = {
        "posts": recent_posts,  # Passar apenas os 30 primeiros posts para o template
    }
    # Renderiza o template da página inicial com os posts recentes.
    return render(request, "blog/index.html", context)



# Exibe os posts filtrados por categoria
def blog_category(request, category):
    # Filtra os posts que pertencem à categoria.
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    # Renderiza o template com os posts da categoria.
    return render(request, "blog/category.html", context)


# Exibe os detalhes de um post específico
def blog_detail(request, pk):
    # Obtém o post pelo ID (chave primária).
    post = get_object_or_404(Post, pk=pk)
    
    # Usa o CommentForm original (forms.Form) para a lógica existente nesta view
    form = CommentForm() 
    if request.method == "POST":
        # Processa o CommentForm original aqui
        form_post = CommentForm(request.POST) # Renomeado para evitar conflito
        if form_post.is_valid():
            comment = Comment(
                author=form_post.cleaned_data["author"],
                body=form_post.cleaned_data["body"],
                post=post,
                # is_approved será False por padrão, conforme seu modelo Comment
            )
            comment.save()
            # Salva o comentário e recarrega a página para mostrar o novo comentário
            return HttpResponseRedirect(request.path_info)

    # Obtém os comentários, reações e avaliações associados ao post.
    comments = Comment.objects.filter(post=post).order_by('created_on') 
    
    reactions = Reaction.objects.filter(post=post)
    ratings = PostRating.objects.filter(post=post)
    
    context = {
        "post": post,
        "comments": comments, # Agora deve conter todos os comentários do post
        "form": form,         # Instância do CommentForm original para o template
        "reactions": reactions,
        "ratings": ratings,
    }
    # Renderiza o template com os detalhes do post.
    return render(request, "blog/detail.html", context)

# Exibe as sugestões de posts enviadas por usuários
def blog_suggestions(request):
    # Obtém todas as sugestões de posts ordenadas pela data de criação.
    suggestions = PostSuggestion.objects.all().order_by("-created_on")
    context = {
        "suggestions": suggestions,
    }
    # Renderiza o template com as sugestões.
    return render(request, "blog/suggestions.html", context)

# Adiciona uma sugestão de post
def submit_suggestion(request):
    if request.method == "POST":
        form = PostSuggestionForm(request.POST)
        if form.is_valid():
            # Salva a sugestão no banco de dados
            form.save() # Funciona porque PostSuggestionForm é um ModelForm
            # Renderiza o template de sucesso
            return render(request, "blog/suggestion_success.html")  
    else:
        form = PostSuggestionForm()
        # Renderiza o formulário de sugestão.
    return render(request, "blog/submit_suggestion.html", {"form": form})

# Criação de enquetes
def create_poll(request):
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário
            question = form.cleaned_data["question"]
            option_one = form.cleaned_data["option_one"]
            option_two = form.cleaned_data["option_two"]
            option_three = form.cleaned_data.get("option_three", None)

            return redirect("poll_success")  # Redirecionar após o envio
    else:
        form = PollForm()
        # Renderiza o formulário de criação de enquetes.
    return render(request, "blog/create_poll.html", {"form": form})

# Página de sucesso após criar uma enquete
def poll_success(request):
    return render(request, 'blog/poll_success.html')  

# Votação em uma enquete
def vote_poll(request, poll_id):
    # Obtém a enquete pelo ID ou retorna 404 se não existir.
    poll = get_object_or_404(VotePoll, id=poll_id)

    if request.method == "POST":
        selected_option = request.POST.get("option")
        if selected_option == "option_one":
            poll.votes_option_one += 1
        elif selected_option == "option_two":
            poll.votes_option_two += 1
        elif selected_option == "option_three" and poll.option_three: # Verifica se option_three existe
            poll.votes_option_three += 1
        poll.save()
        # Salva o voto e redireciona para os resultados.
        return redirect("poll_results", poll_id=poll.id)  
    # Renderiza o template de votação.
    return render(request, "blog/vote_poll.html", {"poll": poll})

# Resultados de uma enquete
def poll_results(request, poll_id):
    poll = get_object_or_404(VotePoll, id=poll_id)
    # Renderiza o template com os resultados da enquete.
    return render(request, "blog/poll_results.html", {"poll": poll})

# Inscrição na newsletter
def newsletter_signup(request):
    if request.method == "POST":
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            # Salvar o e-mail no banco de dados (você precisaria de um modelo para NewsletterSubscriber)
            email = form.cleaned_data["email"]
            # Ex: NewsletterSubscriber.objects.create(email=email)
            # Renderizar o template de sucesso
            return render(request, "blog/newsletter_success.html")
    else:
        form = NewsletterSignupForm()
        # Renderiza o formulário de inscrição.
    return render(request, "blog/newsletter_signup.html", {"form": form})


# Registro de eventos
def register_event(request):
    if request.method == "POST":
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            Event.objects.create( # Assume que Event é seu modelo
                event_name=form.cleaned_data["event_name"],
                date=form.cleaned_data["date"],
                location=form.cleaned_data["location"],
                description=form.cleaned_data["description"],
            )
            # Renderiza o template de sucesso
            return render(request, "blog/event_success.html")
    else:
        form = EventRegistrationForm()
        # Renderiza o formulário de registro de eventos.
    return render(request, "blog/register_event.html", {"form": form})

# Criação de posts no blog
def create_blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            category_name = form.cleaned_data["category"]
            tags_string = form.cleaned_data["tags"]
            
            return render(request, "blog/blog_post_success.html")
    else:
        form = BlogPostForm()
        # Renderiza o formulário de criação de posts.
    return render(request, "blog/create_blog_post.html", {"form": form})

def suggestion_success(request):
    return render(request, "blog/suggestion_success.html")

def event_success(request):
    return render(request, "blog/event_success.html")

def blog_post_success(request):
    return render(request, "blog/blog_post_success.html")

def newsletter_success(request):
    return render(request, "blog/newsletter_success.html")

class CommentListViewCBV(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'
    ordering = ['-created_on']
    paginate_by = 10

class CommentDetailViewCBV(DetailView):
    model = Comment
    template_name = 'blog/comment_detail.html'
    context_object_name = 'comment'

class CommentCreateViewCBV(CreateView):
    model = Comment
    form_class = CommentModelForm
    template_name = 'blog/comment_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.post = self.post_instance
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.post_instance.pk}) + f'#comment-{self.object.pk}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.post_instance
        context['page_title'] = f'Adicionar Comentário em "{self.post_instance.title}" (CBV)'
        return context

class CommentUpdateViewCBV(UpdateView):
    model = Comment
    form_class = CommentModelForm
    template_name = 'blog/comment_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object.post
        context['page_title'] = f'Editar Comentário de {self.object.author} (CBV)'
        return context
    
    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.object.post.pk}) + f'#comment-{self.object.pk}'


class CommentDeleteViewCBV(DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    context_object_name = 'comment'

    def get_success_url(self):
        post_pk = self.object.post.pk
        return reverse('blog_detail', kwargs={'pk': post_pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object.post
        return context

def comment_list_fbv(request):
    comments = Comment.objects.all().order_by('-created_on')
    context = {'comments': comments}
    return render(request, 'blog/comment_list.html', context)

def comment_detail_fbv(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    context = {'comment': comment}
    return render(request, 'blog/comment_detail.html', context)

def comment_create_fbv(request, post_pk):
    post_instance = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post_instance
            comment.save()
            return redirect(reverse('blog_detail', kwargs={'pk': post_instance.pk}) + f'#comment-{comment.pk}')
    else:
        form = CommentModelForm()
    context = {
        'form': form,
        'post': post_instance,
        'page_title': f'Adicionar Comentário em "{post_instance.title}" (FBV)'
    }
    return render(request, 'blog/comment_form.html', context)

def comment_update_fbv(request, pk):
    comment_instance = get_object_or_404(Comment, pk=pk)
    post_instance = comment_instance.post
    if request.method == 'POST':
        form = CommentModelForm(request.POST, instance=comment_instance) # USA O CommentModelForm
        if form.is_valid():
            form.save()
            return redirect(reverse('blog_detail', kwargs={'pk': post_instance.pk}) + f'#comment-{comment_instance.pk}')
    else:
        form = CommentModelForm(instance=comment_instance)
    context = {
        'form': form,
        'comment': comment_instance,
        'post': post_instance,
        'page_title': f'Editar Comentário de {comment_instance.author} (FBV)'
    }
    return render(request, 'blog/comment_form.html', context)

def comment_delete_fbv(request, pk):
    comment_instance = get_object_or_404(Comment, pk=pk)
    post_pk_for_redirect = comment_instance.post.pk
    if request.method == 'POST':
        comment_instance.delete()
        return redirect('blog_detail', pk=post_pk_for_redirect)
    context = {
        'comment': comment_instance,
        'post': comment_instance.post
    }
    return render(request, 'blog/comment_confirm_delete.html', context)

class PostViewSet(viewsets.ModelViewSet):
    """
    Este ViewSet automaticamente fornece as ações `list`, `create`, `retrieve`,
    `update` e `destroy` para o modelo Post.
    """
    queryset = Post.objects.all().order_by('-created_on')
    serializer_class = PostSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Category.
    """
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet para o modelo Comment.
    """
    queryset = Comment.objects.all().order_by('-created_on')
    serializer_class = CommentSerializer
