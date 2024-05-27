from django.contrib.auth.forms import UserCreationForm

from mailings.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'avatar', 'phone_number', 'country']