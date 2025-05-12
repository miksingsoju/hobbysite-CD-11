from django.contrib import admin
from .models import Article, ArticleCategory, Comment, WikiImage
from user_management.models import Profile

class WikiImageInline(admin.StackedInline):
    model = WikiImage
    extra = 4
    fields = ('image', 'description')
    
@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', )
    ordering = ('name', )
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "category", "created_on", "updated_on")
    list_filter = ("category", "created_on")
    search_fields = ("title", )
    ordering = ("-created_on",)  # Sorts articles by newest first
    inlines = [WikiImageInline]
    
    readonly_fields = ("created_on", "updated_on") # Prevents editing of dateandtime
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "article")
    list_filter = ("author", "created_on")
    ordering = ("-created_on", )
    readonly_fields = ("created_on", "updated_on")