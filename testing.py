from datetime import datetime, timedelta

from mailings.models import Newsletter

now = datetime.now()
newsletter_list = Newsletter.objects.filter(date__gte=now)
