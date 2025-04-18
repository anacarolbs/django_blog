from django.contrib import admin
from blog.models import Category, Comment, Post #importar models a serem registradas na pãgina admin

#definir como vazias as classes
class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

#registrar models com admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
