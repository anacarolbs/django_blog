from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Category, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'post_count']

class CommentSerializer(serializers.ModelSerializer):
    short_body = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'body', 'short_body', 'created_on', 'is_approved']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    categories = CategorySerializer(many=True, read_only=True)

    categories_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all(),
        source='categories',
        write_only=True
    )

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'author',
            'created_on',
            'last_modified',
            'categories',
            'categories_ids',
            'comment_count',
            'comments',
        ]
