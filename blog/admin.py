# Register your models here.

from django.contrib import admin
from .models import ArticleCategory, Article

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory

class ArticleAdmin(admin.ModelAdmin):
    model = Article

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategory)


