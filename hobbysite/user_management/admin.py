from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'email_address', 'bio')
    search_fields = ('display_name', 'email_address', 'user__username')