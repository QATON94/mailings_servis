import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import F

from config.settings import EMAIL_HOST_USER
from mailings.models import Newsletter, Reply


def start_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.now(zone)

    mailings = Newsletter.objects.filter(status='запущено')

    for mailing in mailings:
        print(datetime.strftime(now, "%Y-%m-%d %H:%M:%S"))
        print('--------------------------')

        if datetime.strftime(mailing.date_time_start, "%Y-%m-%d %H:%M:%S") <= datetime.strftime(now, "%Y-%m-%d %H:%M:%S"):
            topic = mailing.message.topic
            text = mailing.message.text
            mailing.dispatch_time = mailing.date_time_start
            try_status = ''
            server_response = ''

            try:
                send_mail(
                    subject=topic,
                    message=text,
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[client.email for client in mailing.client.all()],
                    fail_silently=False,
                )
                if mailing.period == 'раз в день':
                    mailing.dispatch_time = mailing.dispatch_time + timedelta(days=1)
                    print(mailing.dispatch_time)
                    print('--------------------------')
                    if datetime.strftime(mailing.dispatch_time, "%Y-%m-%d %H:%M:%S") <= datetime.strftime(
                            mailing.date_time_end, "%Y-%m-%d %H:%M:%S"):
                        mailing.status = 'запущено'
                    else:
                        mailing.status = 'завершено'

                if mailing.period == 'раз в неделю':
                    mailing.dispatch_time = mailing.dispatch_time + timedelta(days=7)
                    if datetime.strftime(mailing.dispatch_time, "%Y-%m-%d %H:%M:%S") <= datetime.strftime(
                            mailing.date_time_end, "%Y-%m-%d %H:%M:%S"):
                        mailing.status = 'запущено'
                    else:
                        mailing.status = 'завершено'

                if mailing.period == 'раз в месяц':
                    mailing.dispatch_time = mailing.dispatch_time + timedelta(days=30)
                    if datetime.strftime(mailing.dispatch_time, "%Y-%m-%d %H:%M:%S") <= datetime.strftime(
                            mailing.date_time_end, "%Y-%m-%d %H:%M:%S"):
                        mailing.status = 'запущено'
                    else:
                        mailing.status = 'завершено'

                mailing.save()
                try_status = 'success'
                server_response = 'успешно'

            except smtplib.SMTPResponseException as error:
                try_status = 'fail'
                server_response = str(error)

            finally:
                reply = Reply.objects.create(last_try_datatime=now, status=try_status,
                                             mail_server_response=server_response)
                reply.save()

        else:
            mailing.status = 'завершено'
            mailing.save()
