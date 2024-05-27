import smtplib
from datetime import datetime, timedelta

from django.core.mail import send_mail
from django.db.models import F

from config.settings import EMAIL_HOST_USER
from mailings.models import Newsletter, Reply


def start_mailing():

    now = datetime.now()
    newsletter_list = Newsletter.objects.filter(date_time_start__gte=now)
    for newsletter in newsletter_list:
        topic = newsletter.message.topic
        text = newsletter.message.text
        newsletter.dispatch_time = newsletter.date_time_start
        try_status = ''
        server_response = ''

        try:
            send_mail(
                subject=topic,
                message=text,
                from_email=EMAIL_HOST_USER,
                recipient_list=[client.email for client in newsletter.client.all()],
                fail_silently=False,
            )
            if newsletter.period == 'раз в день':
                newsletter.dispatch_time = F('dispatch_time') + timedelta(days=1)
                if datetime.strftime(newsletter.dispatch_time, "%Y-%m-%d %H:%M:%S") <= datetime.strftime(
                        newsletter.date_time_end, "%Y-%m-%d %H:%M:%S"):
                    newsletter.status = 'запущено'
                else:
                    newsletter.status = 'завершено'

            if newsletter.period == 'раз в неделю':
                newsletter.dispatch_time = F('dispatch_time') + timedelta(days=7)
                if datetime.strftime(newsletter.dispatch_time, "%Y-%m-%d %H:%M:%S") <= datetime.strftime(
                        newsletter.date_time_end, "%Y-%m-%d %H:%M:%S"):
                    newsletter.status = 'запущено'
                else:
                    newsletter.status = 'завершено'

            if newsletter.period == 'раз в месяц':
                newsletter.dispatch_time = F('dispatch_time') + timedelta(days=30)
                if datetime.strftime(newsletter.dispatch_time, "%Y-%m-%d %H:%M:%S") <= datetime.strftime(
                        newsletter.date_time_end, "%Y-%m-%d %H:%M:%S"):
                    newsletter.status = 'запущено'
                else:
                    newsletter.status = 'завершено'

            try_status = 'success'
            server_response = 'успешно'

        except smtplib.SMTPResponseException as error:
            try_status = 'fail'
            server_response = str(error)

        finally:
            Reply.objects.create(last_try_datatime=now, status=try_status, mail_server_response=server_response)
