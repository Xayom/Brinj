from django.shortcuts import render
from menu.models import Menu


def home(request):
    template = 'index.html'
    context = {}
    context['first'] = Menu.objects.filter(type=1)
    context['second'] = Menu.objects.filter(type=2)
    context['third'] = Menu.objects.filter(type=3)
    context['forth'] = Menu.objects.filter(type=4)
    context['fifth'] = Menu.objects.filter(type=5)
    context['sixth'] = Menu.objects.filter(type=6)

    return render(request, template, context)


def zakaz(request):
    template = 'zakaz.html'
    print(request.POST)
    return render(request, template, {})
