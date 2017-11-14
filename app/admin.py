from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Email, Comment


class MyAdmin(MarkdownxModelAdmin):

    prepopulated_fields = {'slug': ['title']}

admin.site.register(Post, MyAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Email)
