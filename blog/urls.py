from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<str:category>/", views.blog_category, name="blog_category"),  # Ajustado para <str:category>
    path("suggestions/", views.blog_suggestions, name="blog_suggestions"),  # Nova rota para sugestões de post
    path("submit-suggestion/", views.submit_suggestion, name="submit_suggestion"),  # Formulário de sugestão
    path("newsletter-signup/", views.newsletter_signup, name="newsletter_signup"), # Formulário de inscrição na newsletter
    path("register-event/", views.register_event, name="register_event"),
    path("create-poll/", views.create_poll, name="create_poll"),
    path('poll-success/', views.poll_success, name='poll_success'), 
    path("vote-poll/<int:poll_id>/", views.vote_poll, name="vote_poll"),
    path("poll-results/<int:poll_id>/", views.poll_results, name="poll_results"),
]
