from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory, BaseInlineFormSet

from mailings.models import Newsletter, Client, Messages


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        exclude = ['status', 'reply']

        date_time_start = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M')
        date_time_end = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M')


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MessagesForm(ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'
