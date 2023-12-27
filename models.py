# my_app/models.py

from django.db import models
from django.contrib.auth.models import User, Group, Permission

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

# Создание групп и добавление прав
common_group, _ = Group.objects.get_or_create(name='common')
authors_group, _ = Group.objects.get_or_create(name='authors')

post_permissions = Permission.objects.filter(
    content_type__app_label='my_app',  # Замените на ваше приложение
    codename__in=['add_post', 'change_post']
)

authors_group.permissions.add(*post_permissions)
