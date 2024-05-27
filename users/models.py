from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(verbose_name="аватар", upload_to="users/", blank=True, null=True)
    phone_number = models.CharField(max_length=35, verbose_name='Номер телефона', blank=True, null=True,
                                    help_text='Введите номер телефона')
    country = models.CharField(max_length=150, verbose_name='страна', blank=True, null=True, )
    verification_code = models.CharField(max_length=100, verbose_name='код подтверждения', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ('can_view_any_mailings', 'Может просматривать любые рассылки'),
            ('can_view_the_list_of_service_users', 'Может просматривать список пользователей сервиса'),
            ('can_block_service_users.', 'Может блокировать пользователей сервиса'),
            ('can_disable_mailings', 'Может отключать рассылки'),
        ]

    def __str__(self):
        return self.email
