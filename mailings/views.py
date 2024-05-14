from django.shortcuts import render


def base_mil(request):
    template_name = 'mailings/index.html'
    return render(request, template_name)
