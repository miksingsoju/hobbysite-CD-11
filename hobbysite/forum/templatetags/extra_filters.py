from django import template

register = template.Library()

@register.filter    
def anyFromUser(items, user):
    for item in items:
        if item.author == user: return True
    return False
