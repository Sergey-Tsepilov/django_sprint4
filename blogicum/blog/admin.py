from django.contrib import admin

from .models import Location, Category, Post, Comment

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
