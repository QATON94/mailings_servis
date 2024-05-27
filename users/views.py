import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from config import settings
from config.settings import CHARS
from users.froms import UserRegisterForm
from users.models import User


class RegisterUserView(CreateView):
    model = User
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse_lazy('users:confirm')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация пользователя'
        return context

    def form_valid(self, form):
        user = form.save()
        user.is_active = False

        current_site = self.request.get_host()

        subject = 'Подтверждение регистрации'

        verification_code = ''.join(str(random.randint(1, 10)) for _ in range(9))
        user.verification_code = verification_code

        message = (f'Вы успешно зарегистрировались на нашем сайте. Чтобы продолжить использовать необходимо'
                   f'подтвердить регистрацию по ссылке http://{current_site}/users/confirm/ и ввести код '
                   f'{verification_code}')
        user.save()
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email, ],
        )
        print(send_mail)
        user.save()

        return super().form_valid(form)


class Logout(LoginRequiredMixin, LogoutView):
    pass


class ConfirmRegistrationUserView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'users/confirm_registration.html')

    def post(self, request, *args, **kwargs):
        verification_code = request.POST.get('verification_code')
        user = get_object_or_404(User, verification_code=verification_code)

        if user:
            user.is_active = True
            user.save()
            return redirect('users:login')
        return redirect('mailings:home')


def reset_password(request):
    password = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        for i in range(10):
            password += random.choice(CHARS)
        subject = 'Восстановление пароля'
        message = f'Вы успешно сбросили пароль. Ваш новый пароль: {password}'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email, ],
        )
        user.set_password(password)
        user.save()
        return redirect('users:login')
    return render(request, 'users/password_reset_form.html')
