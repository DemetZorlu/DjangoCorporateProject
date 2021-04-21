from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Setting


def index(request):
    setting = Setting.objects.all()
    context = {'setting': setting[0]}
    return render(request, 'index.html', context)
