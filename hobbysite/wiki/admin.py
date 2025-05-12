from django.contrib import admin
from .models import Article, ArticleCategory
    
@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', )
    ordering = ('name', )
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "created_on", "updated_on")
    list_filter = ("category", "created_on")
    search_fields = ("title", )
    ordering = ("-created_on",)  # Sorts articles by newest first
    
    readonly_fields = ("created_on", "updated_on") # Prevents editing of dateandtime