from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailings.forms import NewsletterForm, ClientForm, MessagesForm
from mailings.models import Newsletter, Client, Messages


def base_mil(request):
    template_name = 'mailings/index.html'
    return render(request, template_name)


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterCreateView(CreateView):
    model = Messages
    form_class = NewsletterForm
    success_url = reverse_lazy('mailings:newsletter_list')

    # def form_valid(self, form):
    #     """Добавление пользователя к клиенту"""
    #     self.object = form.save()
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('mailings:newsletter_list')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('mailings:newsletter_list')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client
    success_url = reverse_lazy('mailings:client_list')


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        clients = Client.objects.all()
        context['clients'] = clients
        return context


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        return context


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:client_list')


class MessagesListView(ListView):
    model = Messages


class MessagesDetailView(DetailView):
    model = Messages


class MessagesCreateView(CreateView):
    model = Messages
    form_class = MessagesForm
    success_url = reverse_lazy('mailings:messages_list')


class MessagesUpdateView(UpdateView):
    model = Messages
    form_class = MessagesForm
    success_url = reverse_lazy('mailings:messages_list')


class MessagesDeleteView(DeleteView):
    model = Messages
    success_url = reverse_lazy('mailings:messages_list')
