from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'publish', 'created', 'author')
    search_fields = ('title', 'body', 'author')
    preserve_filters = {'slug': ['title']}
    date_hierarchy = 'publish'
    ordering = ('publish', 'status')