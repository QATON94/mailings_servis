from django import forms
from django.forms import ModelForm, BooleanField

from mailings.models import Newsletter, Client, Messages


class StyleFormMixin:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class NewsletterForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Newsletter
        exclude = ['status', 'reply', 'user', 'dispatch_time']

        date_time_start = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M')
        date_time_end = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M')


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        exclude = ['user']


class MessagesForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Messages
        exclude = ['user']


class ManagerNewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['status']
