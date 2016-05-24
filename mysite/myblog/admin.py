from django.contrib import admin

from myblog.models import Category
from myblog.models import Post

class DetailInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [
        DetailInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
#    inlines = [
#        DetailInline,
#    ]
    exclude = ('posts',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
