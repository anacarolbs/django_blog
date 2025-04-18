from django.contrib import admin
from blog.models import Category, Comment, Post, Reaction, PostRating, PostSuggestion #importar models a serem registradas na pãgina admin

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

#registrar models com admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reaction, ReactionAdmin)
admin.site.register(PostRating, PostRatingAdmin)
admin.site.register(PostSuggestion, PostSuggestionAdmin)