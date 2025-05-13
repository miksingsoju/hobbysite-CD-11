from django.contrib import admin
from .models import ThreadCategory, Thread, Comment

class ThreadCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ('name',)

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'updated_on')
    list_filter = ('author', 'category', 'created_on', 'updated_on')
    search_fields = ('title', 'author', 'entry')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_on', 'updated_on')
    list_filter = ('author', 'thread', 'created_on', 'updated_on')
    search_fields = ('author', 'thread', 'entry')

admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Comment, CommentAdmin)
