from django.core.management import BaseCommand

from mailings.services import start_mailing


class Command(BaseCommand):
    def handle(self, *args, **options):
        start_mailing()
