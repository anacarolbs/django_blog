from django.shortcuts import render, redirect
#import models
from blog.models import Post, Comment, Category, Reaction, PostRating, PostSuggestion
from django.http import HttpResponseRedirect
from blog.forms import CommentForm

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
