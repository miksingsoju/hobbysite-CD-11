from django.contrib import admin
from .models import Article, ArticleCategory
    
@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', )
    ordering = ('name', )
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_on", "updated_on")  # Admin columns
    list_filter = ("category", "created_on")  # Adds filters in the right sidebar
    search_fields = ("title", "entry")  # Allows searching by title & content
    ordering = ("-created_on",)  # Sorts articles by newest first
    date_hierarchy = "created_on"  # Adds a date-based navigation filter

    fieldsets = (
        ("Basic Info", {"fields": ("title", "category")}),
        ("Content", {"fields": ("entry",)}),
        ("Timestamps", {"fields": ("created_on", "updated_on")}),
    )
    
    readonly_fields = ("created_on", "updated_on") # Prevents editing of dateandtime