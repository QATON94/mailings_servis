from django.db import models

from users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name='Статья')
    image = models.ImageField(upload_to="blog/image", null=True, blank=True, verbose_name='изображение')
    number_views = models.IntegerField(default=0, verbose_name='количество просмотров')
    date_publications = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', null=True, blank=True)
    publication_sign = models.BooleanField(verbose_name='признак публикации', default=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['title', 'date_publications']

