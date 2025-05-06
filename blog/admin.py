from django.contrib import admin
from blog.models import Category, Comment, Post, Reaction, PostRating, PostSuggestion, VotePoll 

# Define classes de administração para personalizar a interface de administração.

#definir como vazias as classes
class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class ReactionAdmin(admin.ModelAdmin):
    pass

class PostRatingAdmin(admin.ModelAdmin):
    pass

class PostSuggestionAdmin(admin.ModelAdmin):
    pass

# Registra os modelos no painel de administração com suas respectivas classes de administração.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reaction, ReactionAdmin)
admin.site.register(PostRating, PostRatingAdmin)
admin.site.register(PostSuggestion, PostSuggestionAdmin)

@admin.register(VotePoll)
# Personaliza a exibição do modelo `VotePoll` no painel de administração.
class VotePollAdmin(admin.ModelAdmin):
    # Exibe as colunas `question`, `votes_option_one`, `votes_option_two` e `votes_option_three` na lista de enquetes.
    list_display = ("question", "votes_option_one", "votes_option_two", "votes_option_three")