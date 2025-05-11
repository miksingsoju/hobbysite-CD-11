from django import template

# Extra filters registered to the template library. These assist 
# with filtering done in the thread list template and its base. 

register = template.Library()

@register.filter    
def anyFromUser(items, user):
    for item in items:
        if item.author == user: return True
    return False

@register.filter    
def anyFromOther(items, user):
    for item in items:
        if item.author != user: return True
    return False