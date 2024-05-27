from time import sleep

from django.apps import AppConfig



class MailingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailings'

    # def ready(self):
    #     # from .management.commands.start_schedule import start_mailing
    #     # sleep(5)
    #     from mailings.services import start_mailing
    #     sleep(1)
    #     start_mailing()
