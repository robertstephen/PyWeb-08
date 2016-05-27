from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

from myblog.models import Category
from myblog.models import Post

class DetailInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [
        DetailInline,
    ]
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
#    author = models.ForeignKey(User)

class CategoryAdmin(admin.ModelAdmin):
#    inlines = [
#        DetailInline,
#    ]
    exclude = ('posts',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
