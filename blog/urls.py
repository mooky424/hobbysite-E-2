from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView

urlpatterns = [
   path('articles', ArticleListView.as_view(), name = 'articles'),
   path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article_detail'),
   path('article/add/', ArticleCreateView.as_view(), name='create_article'),
   path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
] 

app_name = "blog"