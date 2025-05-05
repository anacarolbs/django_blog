from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Comment, Category, Reaction, PostRating, PostSuggestion, VotePoll
from django.http import HttpResponseRedirect
from blog.forms import CommentForm, PollForm, BlogPostForm, PostSuggestionForm, NewsletterSignupForm, EventRegistrationForm



# Exibe todos os posts do blog
def blog_index(request):
    #obtain a Queryset containing all the posts in the database. A Queryset is a collection of all the objects in the database that match the query.
    posts = Post.objects.all().order_by("-created_on") # (-): get the recently created posts first
    context = {
        "posts": posts,
    }
    #define a context dictionary and render a template named index.html
    return render(request, "blog/index.html", context)


# Exibe os posts filtrados por categoria
def blog_category(request, category):
    # Django Queryset filter. The argument of the filter tells Django what conditions need to be true to retrieve an object. 
    # In this case, you only want posts whose categories contain the category with the name corresponding to what’s given in the argument of the view function.
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


# Exibe os detalhes de um post específico
def blog_detail(request, pk):
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
            return HttpResponseRedirect(request.path_info)


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
    
    return render(request, "blog/detail.html", context)

# Exibe as sugestões de posts enviadas por usuários
def blog_suggestions(request):
    suggestions = PostSuggestion.objects.all().order_by("-created_on")
    context = {
        "suggestions": suggestions,
    }
    return render(request, "blog/suggestions.html", context)

# Adiciona uma sugestão de post
def submit_suggestion(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        user = request.user if request.user.is_authenticated else None  # Usuário opcional

        if title and description:
            PostSuggestion.objects.create(user=user, title=title, description=description)
            return redirect("blog_suggestions")

    return render(request, "blog/submit_suggestion.html")

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
    return render(request, "blog/create_poll.html", {"form": form})

def poll_success(request):
    return render(request, 'blog/poll_success.html')  

def vote_poll(request, poll_id):
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
        return redirect("poll_results", poll_id=poll.id)  # Redirecionar para os resultados

    return render(request, "blog/vote_poll.html", {"poll": poll})

def poll_results(request, poll_id):
    poll = get_object_or_404(VotePoll, id=poll_id)
    return render(request, "blog/poll_results.html", {"poll": poll})

def submit_suggestion(request):
    if request.method == "POST":
        form = PostSuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog_index")  # Redirecionar após o envio
    else:
        form = PostSuggestionForm()
    return render(request, "blog/submit_suggestion.html", {"form": form})


def newsletter_signup(request):
    if request.method == "POST":
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            # salvar o e-mail no banco de dados ou enviar para um serviço de newsletter
            email = form.cleaned_data["email"]
            # Exemplo: salvar no banco de dados (crie um modelo NewsletterSubscriber, se necessário)
            # NewsletterSubscriber.objects.create(email=email)
            return redirect("blog_index")  # Redirecionar após o cadastro
    else:
        form = NewsletterSignupForm()
    return render(request, "blog/newsletter_signup.html", {"form": form})

def register_event(request):
    if request.method == "POST":
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            # Salvar os dados no banco ou processá-los
            event_name = form.cleaned_data["event_name"]
            date = form.cleaned_data["date"]
            location = form.cleaned_data["location"]
            description = form.cleaned_data["description"]
            # Exemplo: salvar no banco de dados (crie um modelo Event, se necessário)
            # Event.objects.create(event_name=event_name, date=date, location=location, description=description)
            return redirect("blog_index")  # Redirecionar após o envio
    else:
        form = EventRegistrationForm()
    return render(request, "blog/register_event.html", {"form": form})

def create_blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            # Processar os dados do formulário
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            category = form.cleaned_data["category"]
            tags = form.cleaned_data["tags"]
            # Exemplo: salvar no banco de dados (crie um modelo BlogPost, se necessário)
            # BlogPost.objects.create(title=title, content=content, category=category, tags=tags)
            return redirect("blog_index")  # Redirecionar após o envio
    else:
        form = BlogPostForm()
    return render(request, "blog/create_blog_post.html", {"form": form})