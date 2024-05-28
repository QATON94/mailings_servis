from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailings.forms import NewsletterForm, ClientForm, MessagesForm, ManagerNewsletterForm
from mailings.models import Newsletter, Client, Messages, Reply


def base_mil(request):
    template_name = 'mailings/index.html'
    return render(request, template_name)


class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Messages
    form_class = NewsletterForm
    success_url = reverse_lazy('mailings:newsletter_list')

    def form_valid(self, form):
        """Добавление пользователя к клиенту"""
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('mailings:newsletter_list')

    def get_form_class(self):
        if self.request.user == self.object.user or self.request.user.is_superuser:
            return NewsletterForm
        elif self.request.user.has_perm('mailing.set_deactivate'):
            return ManagerNewsletterForm
        else:
            raise Http404('У вас нет прав на редактирование рассылок')


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mailings:newsletter_list')

    def get_form_class(self):
        if self.request.user == self.object.user or self.request.user.is_superuser:
            return NewsletterDeleteView
        else:
            raise Http404('У вас нет прав на удаление рассылок')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    success_url = reverse_lazy('mailings:client_list')


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = Client.objects.all()
        context['clients'] = clients
        return context

    def form_valid(self, form):
        """Добавление пользователя к клиенту"""
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        return context

    def get_form_class(self):
        if self.request.user == self.object.user or self.request.user.is_superuser:
            return ClientForm
        else:
            raise Http404('У вас нет прав на редактирование клиентов')


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:client_list')

    def get_form_class(self):
        if self.request.user == self.object.user or self.request.user.is_superuser:
            return ClientDeleteView
        else:
            raise Http404('У вас нет прав на удаление клиента')


class MessagesListView(LoginRequiredMixin, ListView):
    model = Messages


class MessagesDetailView(DetailView):
    model = Messages


class MessagesCreateView(LoginRequiredMixin, CreateView):
    model = Messages
    form_class = MessagesForm
    success_url = reverse_lazy('mailings:messages_list')


class MessagesUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Messages
    form_class = MessagesForm
    success_url = reverse_lazy('mailings:messages_list')

    def get_form_class(self):
        if self.request.user == self.object.user or self.request.user.is_superuser:
            return ClientForm
        else:
            raise Http404('У вас нет прав на редактирование сообщений')


class MessagesDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Messages
    success_url = reverse_lazy('mailings:messages_list')

    def get_form_class(self):
        if self.request.user == self.object.user or self.request.user.is_superuser:
            return ClientDeleteView
        else:
            raise Http404('У вас нет прав на удаление сообщений')


class ReplyListView(LoginRequiredMixin, ListView):
    model = Reply


class ReplyDetailView(LoginRequiredMixin, DetailView):
    model = Reply


class ReplyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Reply
    success_url = reverse_lazy('mailings:reply_list')

    def get_form_class(self):
        if self.request.user == self.object.user or self.request.user.is_superuser:
            return ClientDeleteView
        else:
            raise Http404('У вас нет прав на удаление логов')
