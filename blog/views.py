from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Comment, Category, Reaction, PostRating, PostSuggestion, VotePoll, Event
from django.http import HttpResponseRedirect
from blog.forms import CommentForm, PollForm, BlogPostForm, PostSuggestionForm, NewsletterSignupForm, EventRegistrationForm

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
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            # Salva o comentário e recarrega a página.
            return HttpResponseRedirect(request.path_info)

# Obtém os comentários, reações e avaliações associados ao post.
    comments = Comment.objects.filter(post=post)
    reactions = Reaction.objects.filter(post=post)
    ratings = PostRating.objects.filter(post=post)
    
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
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
            form.save()
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
            # Poll.objects.create(question=question, option_one=option_one, option_two=option_two, option_three=option_three)
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
        elif selected_option == "option_three":
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
            # Salvar o e-mail no banco de dados 
            email = form.cleaned_data["email"]

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
            # Criar uma instância do modelo Event e salvar os dados
            Event.objects.create(
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
            category = form.cleaned_data["category"]
            tags = form.cleaned_data["tags"]

            # Renderizar o template de sucesso
            return render(request, "blog/blog_post_success.html")
    else:
        form = BlogPostForm()
        # Renderiza o formulário de criação de posts.
    return render(request, "blog/create_blog_post.html", {"form": form})

# Páginas de sucesso
def suggestion_success(request):
    return render(request, "blog/suggestion_success.html")

def event_success(request):
    return render(request, "blog/event_success.html")

def blog_post_success(request):
    return render(request, "blog/blog_post_success.html")

def newsletter_success(request):
    return render(request, "blog/newsletter_success.html")    