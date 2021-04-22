from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Setting


def index(request):
    setting = Setting.objects.all()
    context = {'setting': setting[0], 'page': 'home'}
    return render(request, 'index.html', context)


def contact(request):
    setting = Setting.objects.all()
    context = {'setting': setting[0], 'page': 'contact', 'pagename': 'İletişim'}
    return render(request, 'contact.html', context)


def about(request):
    setting = Setting.objects.all()
    context = {'setting': setting[0], 'page': 'about', 'pagename': 'Hakkımızda'}
    return render(request, 'about.html', context)


def referances(request):
    setting = Setting.objects.all()
    context = {'setting': setting[0], 'page': 'referances', 'pagename': 'Referanslarımız'}
    return render(request, 'referances.html', context)
