from django.contrib import admin
from .models import Comment, Commission

# Register your models here.
class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    search_fields = ('title','description', 'people_required', 'created_on','updated_on',)
    list_display = ('title','description', 'people_required', 'created_on','updated_on',)

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    search_fields = ('commission','entry', 'created_on','updated_on',)
    list_display = ('commission','entry', 'created_on','updated_on',)

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)