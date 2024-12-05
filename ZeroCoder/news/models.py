from django.db import models
from django.contrib.auth.models import User  # Если буду связывать с моделью пользователя

class NewsPost(models.Model):
    title = models.CharField('Название новости', max_length=100)
    short_description = models.CharField('Краткое описание новости', max_length=255)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.CharField('Автор публикации', max_length=100)
    # Если буду связывать с моделью пользователя:
    # author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'