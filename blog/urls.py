from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<str:category>/", views.blog_category, name="blog_category"),  # Ajustado para <str:category>
    path("suggestions/", views.blog_suggestions, name="blog_suggestions"),  # Nova rota para sugestões de post
    path("submit-suggestion/", views.submit_suggestion, name="submit_suggestion"),  # Formulário de sugestão
]
