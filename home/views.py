from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from content.models import Content
from home.models import Setting, ContactFormu, ContactFormMessage


def index(request):
    setting = Setting.objects.all()
    sliderdata = Content.objects.filter(type=4, status="True")
    context = {'setting': setting[0], 'page': 'home', 'sliderdata': sliderdata}
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız gönderilmiştir. Teşekkür ederiz.")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.all()
    form = ContactFormu()
    context = {'setting': setting[0], 'page': 'contact', 'pagename': 'İletişim', 'form': form}
    return render(request, 'contact.html', context)


def about(request):
    setting = Setting.objects.all()
    context = {'setting': setting[0], 'page': 'about', 'pagename': 'Hakkımızda'}
    return render(request, 'about.html', context)


def referances(request):
    setting = Setting.objects.all()
    context = {'setting': setting[0], 'page': 'referances', 'pagename': 'Referanslarımız'}
    return render(request, 'referances.html', context)


def academiccalendar(request):
    setting = Setting.objects.all()
    context = {'setting': setting[0], 'page': 'academiccalendar', 'pagename': 'Akademik Takvim'}
    return render(request, 'academiccalendar.html', context)
