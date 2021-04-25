from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from content.models import Content, Menu, Images
from home.models import Setting, ContactFormu, ContactFormMessage


def index(request):
    setting = Setting.objects.all()
    sliderdata = Content.objects.filter(type=4, status="True")
    newsdata = Content.objects.filter(type=2, status="True")
    announcementdata = Content.objects.filter(type=3, status="True")
    activitiesdata = Content.objects.filter(type=5, status="True")
    menu = Menu.objects.filter(status="True")
    context = {'menu': menu, 'setting': setting[0], 'page': 'home', 'sliderdata': sliderdata, 'newsdata': newsdata,
               'announcementdata': announcementdata, 'activitiesdata': activitiesdata}
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
    menu = Menu.objects.filter(status="True")
    context = {'menu': menu, 'setting': setting[0], 'page': 'contact', 'pagename': 'İletişim', 'form': form}
    return render(request, 'contact.html', context)


def about(request):
    setting = Setting.objects.all()
    menu = Menu.objects.filter(status="True")
    context = {'menu': menu, 'setting': setting[0], 'page': 'about', 'pagename': 'Hakkımızda'}
    return render(request, 'about.html', context)


def referances(request):
    setting = Setting.objects.all()
    menu = Menu.objects.filter(status="True")
    context = {'menu': menu, 'setting': setting[0], 'page': 'referances', 'pagename': 'Referanslarımız'}
    return render(request, 'referances.html', context)


def academiccalendar(request):
    setting = Setting.objects.all()
    menu = Menu.objects.filter(status="True")
    context = {'menu': menu, 'setting': setting[0], 'page': 'academiccalendar', 'pagename': 'Akademik Takvim'}
    return render(request, 'academiccalendar.html', context)


def academiccontentlist(request, id, slug):
    setting = Setting.objects.all()
    menu = Menu.objects.filter(status="True")
    menucondata = menu.get(pk=id)
    contents = Content.objects.filter(menu_id=id)
    context = {'menu': menu, 'contents': contents, 'setting': setting[0],
               'page': 'academiccontentlist/%d/%s' % (id, slug),
               'pagename': menucondata.title, 'subtitle': menucondata.subtitle, 'menudata': menucondata}
    return render(request, 'contentlist.html', context)


def contentdetail(request, id, slug):
    setting = Setting.objects.all()
    menu = Menu.objects.filter(status="True")
    content = Content.objects.get(pk=id)
    menucondata = Menu.objects.get(pk=content.menu_id)
    images=Images.objects.filter(content_id=id)
    title = ""

    if content.type == 4:
        title = "Gündem"
    elif content.type == 2:
        title = "Haber"
    elif content.type == 3:
        title = "Duyuru"
    elif content.type == 5:
        title = "Etkinlik"
    else:
        title = content.title

    context = {'menu': menu, 'content': content, 'setting': setting[0],
               'page': 'contentdetail/%d/%s' % (id, slug),
               'pagename': title, 'subtitle': menucondata.subtitle, 'menucondata': menucondata, 'images':images}
    return render(request, 'contentdetail.html', context)
