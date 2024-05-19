from django.contrib import admin

from mailings.models import Newsletter, Client, Messages, Reply


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('date_time_start', 'date_time_end', 'period', 'status', 'message')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'lastname', 'Firstname', 'Patronymic', 'email', 'comment')


@admin.register(Messages)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('topic', 'text')


@admin.register(Reply)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_try_datatime', 'status', 'mail_server_response')
