from django.contrib import admin
from .models import Article, ArticleCategory, Comment

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display  = ('title', 'author', 'category', 'created_on', 'updated_on')
    list_filter   = ('author', 'category', 'created_on')
    search_fields = ('title', 'entry')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display  = ('article', 'author', 'created_on')
    list_filter   = ('author', 'article')
    search_fields = ('entry',)
