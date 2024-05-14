from django.urls import path

from mailings.views import base_mil

app_name = 'mailings'

urlpatterns = [
    path('', base_mil, name='home'),
]