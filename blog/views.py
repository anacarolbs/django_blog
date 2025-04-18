from django.shortcuts import render
#import the Post and the Comment models
from blog.models import Post, Comment
from django.http import HttpResponseRedirect
from blog.forms import CommentForm

#blog_index() will display a list of all your posts
def blog_index(request):
    #obtain a Queryset containing all the posts in the database. A Queryset is a collection of all the objects in the database that match the query.
    posts = Post.objects.all().order_by("-created_on") # (-): get the recently created posts first
    context = {
        "posts": posts,
    }
    #define a context dictionary and render a template named index.html
    return render(request, "blog/index.html", context)


#blog_detail() will display the full post. Later, this view will also show existing comments and a form to allow users to create new comments.
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


#blog_category() will be similar to blog_index, but the posts shown will only be of a specific category that the user chooses.
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
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "blog/detail.html", context)