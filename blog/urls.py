# blog/urls.py
from django.urls import path, include # Adicione 'include'
from . import views # Seu import existente

from rest_framework.routers import DefaultRouter
# Importe os ViewSets que você criou em blog/views.py
# (Post, Category, Comment já estão importados em views.py a partir de models)
# Os ViewSets são classes, então precisamos importá-los se estiverem no mesmo arquivo views.py
# ou de api_views.py se você os separou. No nosso caso, estão em views.py:
# (Não precisamos importar os ViewSets aqui diretamente, pois o 'views' já está importado
# e os usaremos como views.NomeDoViewSet ao registrar no router)

# --- CONFIGURAÇÃO DO ROUTER PARA A API ---
router = DefaultRouter()
# Registra os ViewSets com o router.
# O primeiro argumento é o prefixo da URL para este ViewSet (ex: 'api/posts/').
# O segundo é a classe ViewSet.
# O 'basename' é usado para gerar os nomes das URLs. Se o queryset estiver definido no ViewSet,
# o DRF pode inferir isso, mas é bom ser explícito.
router.register(r'posts', views.PostViewSet, basename='post-api')
router.register(r'categories', views.CategoryViewSet, basename='category-api')
router.register(r'comments', views.CommentViewSet, basename='comment-api')


urlpatterns = [
    # ... (SUAS URLs EXISTENTES LISTADAS ACIMA) ...
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<str:category>/", views.blog_category, name="blog_category"),
    path("suggestions/", views.blog_suggestions, name="blog_suggestions"),
    path("submit-suggestion/", views.submit_suggestion, name="submit_suggestion"),
    path("newsletter-signup/", views.newsletter_signup, name="newsletter_signup"),
    path("register-event/", views.register_event, name="register_event"),
    path("create-poll/", views.create_poll, name="create_poll"),
    path('poll-success/', views.poll_success, name='poll_success'), 
    path("vote-poll/<int:poll_id>/", views.vote_poll, name="vote_poll"),
    path("poll-results/<int:poll_id>/", views.poll_results, name="poll_results"),
    path("create-post/", views.create_blog_post, name="create_blog_post"),
    path('suggestion-success/', views.suggestion_success, name='suggestion_success'),
    path('event-success/', views.event_success, name='event_success'),
    path('blog-post-success', views.blog_post_success, name='blog_post_success'),
    path('newsletter-success', views.newsletter_success, name='newsletter_success'),

    # URLs para CBVs de Comentários
    path('comments-cbv/', views.CommentListViewCBV.as_view(), name='comment_list_all_cbv'),
    path('post/<int:post_pk>/comment-cbv/new/', views.CommentCreateViewCBV.as_view(), name='comment_create_cbv'),
    path('comment-cbv/<int:pk>/', views.CommentDetailViewCBV.as_view(), name='comment_detail_cbv'),
    path('comment-cbv/<int:pk>/edit/', views.CommentUpdateViewCBV.as_view(), name='comment_update_cbv'),
    path('comment-cbv/<int:pk>/delete/', views.CommentDeleteViewCBV.as_view(), name='comment_delete_cbv'),

    # URLs para FBVs de Comentários
    path('comments-fbv/', views.comment_list_fbv, name='comment_list_all_fbv'),
    path('post/<int:post_pk>/comment-fbv/new/', views.comment_create_fbv, name='comment_create_fbv'),
    path('comment-fbv/<int:pk>/', views.comment_detail_fbv, name='comment_detail_fbv'),
    path('comment-fbv/<int:pk>/edit/', views.comment_update_fbv, name='comment_update_fbv'),
    path('comment-fbv/<int:pk>/delete/', views.comment_delete_fbv, name='comment_delete_fbv'),

    # --- ADICIONE AS URLS DA API GERADAS PELO ROUTER ---
    # Todas as URLs registradas no 'router' serão incluídas sob o prefixo 'api/'
    # Por exemplo: /blog/api/posts/, /blog/api/categories/, /blog/api/comments/
    path('api/', include(router.urls)),
]
