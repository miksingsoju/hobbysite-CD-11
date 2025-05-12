from django.contrib import admin
from .models import PostCategory, Post

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'updated_on')
    list_filter = ('category', 'created_on')
    search_fields = ('title', 'entry')

admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)