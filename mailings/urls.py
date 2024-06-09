from django.urls import path
from django.views.decorators.cache import cache_page

from mailings.views import HomePageView, NewsletterCreateView, ClientCreateView, NewsletterListView, \
    NewsletterDetailView, NewsletterUpdateView, MessagesUpdateView, ClientUpdateView, NewsletterDeleteView, \
    ClientListView, ClientDetailView, ClientDeleteView, MessagesListView, MessagesDetailView, MessagesCreateView, \
    MessagesDeleteView, ReplyListView, ReplyDetailView, ReplyDeleteView

app_name = 'mailings'

urlpatterns = [
    path('', cache_page(20)(HomePageView.as_view()), name='home'),

    path('newsletter_list', NewsletterListView.as_view(), name='newsletter_list'),
    path('newsletter_view/<int:pk>', NewsletterDetailView.as_view(), name='view_newsletter'),
    path('create_newsletter', NewsletterCreateView.as_view(), name='create_newsletter'),
    path('edit_newsletter/<int:pk>', NewsletterUpdateView.as_view(), name='edit_newsletter'),
    path('delete_newsletter/<int:pk>', NewsletterDeleteView.as_view(), name='delete_newsletter'),

    path('client_list', ClientListView.as_view(), name='client_list'),
    path('client_view/<int:pk>', ClientDetailView.as_view(), name='client_view'),
    path('create_client', ClientCreateView.as_view(), name='create_client'),
    path('edit_client/<int:pk>', ClientUpdateView.as_view(), name='edit_client'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),

    path('messages_list', MessagesListView.as_view(), name='messages_list'),
    path('messages_view/<int:pk>', MessagesDetailView.as_view(), name='messages_view'),
    path('create_messages', MessagesCreateView.as_view(), name='create_messages'),
    path('edit_messages/<int:pk>', MessagesUpdateView.as_view(), name='edit_messages'),
    path('delete_messages/<int:pk>', MessagesDeleteView.as_view(), name='delete_messages'),

    path('reply_list', ReplyListView.as_view(), name='reply_list'),
    path('reply_view/<int:pk>', ReplyDetailView.as_view(), name='reply_view'),
    path('delete_reply/<int:pk>', ReplyDeleteView.as_view(), name='delete_reply'),
]
