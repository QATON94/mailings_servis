from django.db import models


class Client(models.Model):
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)
    lastname = models.CharField(max_length=100, verbose_name="Фамилия")
    Firstname = models.CharField(max_length=100, verbose_name="Имя")
    Patronymic = models.CharField(max_length=100, verbose_name="Отчество")
    comment = models.TextField(verbose_name="Коментарий", blank=True, null=True)

    def __str__(self):
        return f'{self.lastname} {self.Firstname} {self.Patronymic}'

    class Meta:
        db_table = 'client'
        verbose_name = "Клиент сервис"
        verbose_name_plural = "Клиенты сервиса"


class Messages(models.Model):
    topic = models.CharField(max_length=150, verbose_name='Тема письма')
    text = models.TextField(verbose_name='Текст письма')

    class Meta:
        db_table = 'message'
        verbose_name = 'Сообщение для рассылки'


class Reply(models.Model):
    STATUS_CHOICES = [
        ('success', 'успешно'),
        ('fail', 'неуспешно'),
    ]

    last_try_datatime = models.DateTimeField(auto_now=True, verbose_name='дата и время последней попытки')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name='статус попытки', blank=True,
                              null=True)
    mail_server_response = models.TextField(verbose_name='ответ почтового сервера', blank=True, null=True)

    class Meta:
        db_table = 'reply'
        verbose_name = 'Попытка рассылки'


class Newsletter(models.Model):
    DAY = 'раз в день'
    WEEK = 'раз в неделю'
    MONTH = 'раз в месяц'
    PERIOD_TYPE = ((DAY, 'раз в день'), (WEEK, 'раз в неделю'), (MONTH, 'раз в месяц'),)
    COMPLETED = 'завершено'
    CREATE = 'создано'
    LAUNCH = 'запущено'
    STATUS_TYPE = ((COMPLETED, 'завершено'), (LAUNCH, 'запущено'), (CREATE, 'создано'),)

    date_time_start = models.DateTimeField(verbose_name='дата и время первой отправки рассылки')
    dispatch_time = models.DateTimeField(blank=True, null=True, verbose_name='время отправки')
    date_time_end = models.DateTimeField(verbose_name='дата и время последней отправки рассылки')
    period = models.CharField(max_length=50, default=DAY, choices=PERIOD_TYPE)
    status = models.CharField(max_length=50, default=CREATE, choices=STATUS_TYPE)
    client = models.ManyToManyField(Client, verbose_name='Клиент')
    message = models.ForeignKey(Messages, verbose_name='Сообщение', on_delete=models.SET_NULL, blank=True, null=True)
    reply = models.ManyToManyField(Reply, verbose_name='Попытка рассылки')

    class Meta:
        db_table = 'newsletter'
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
