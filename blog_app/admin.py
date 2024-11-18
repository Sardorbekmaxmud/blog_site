from django.contrib import admin
from .models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'publish', 'created', 'author')
    search_fields = ('title', 'body', 'author__username')
    prepopulated_fields = {'slug': ['title']}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    readonly_fields = ['created', 'updated']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('updated', 'created', 'active')
    search_fields = ('name', 'email', 'body')
    readonly_fields = ('created', 'updated')
