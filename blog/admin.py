from django.contrib import admin

from .models import Author, Post, Tag

# Register your models here.

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)