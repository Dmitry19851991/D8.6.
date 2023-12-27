# my_app/urls.py

from django.urls import path
from .views import NewsListView, PostDetailView, CreatePostView

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    # Добавьте другие маршруты, если необходимо
]
