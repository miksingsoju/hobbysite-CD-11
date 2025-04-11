from django.db import models

# PostCategory
# Name - max length is 255 characters
# Description - text field
# Categories should be sorted by name in ascending order

# Post
# Title - max length is 255 characters
# Category - foreign key to PostCategory, sets to NULL when deleted
# Entry - text field
# Created On - datetime field, only gets set when the model is created
# Updated On - datetime field, always updates on last model update
# Posts should be sorted by the date it was created, in descending order

class PostCategory(models.Model):
    pass

class Post(models.Model):
    pass

