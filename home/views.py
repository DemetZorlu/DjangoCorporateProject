import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from content.models import Content, Menu, Images, Comment
from home.forms import SearchForm
from home.models import Setting, ContactFormu, ContactFormMessage, FAQ


def index(request):
    setting = Setting.objects.all()
    sliderdata = Content.objects.filter(type=4, status="True")
    newsdata = Content.objects.filter(type=2, status="True")
    announcementdata = Content.objects.filter(type=3, status="True")
    activitiesdata = Content.objects.filter(type=5, status="True")
    menu = Menu.objects.filter(status="True")
    menusearch = Menu.objects.all()
    context = {'menu': menu,
               'menusearch': menusearch,
               'setting': setting[0],
               'page': 'home',
               'sliderdata': sliderdata,
               'newsdata': newsdata,
               'announcementdata': announcementdata,
               'activitiesdata': activitiesdata}
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
    menusearch = Menu.objects.all()
    context = {'menu': menu,
               'menusearch': menusearch,
               'setting': setting[0],
               'page': 'contact',
               'pagename': 'İletişim',
               'form': form}
    return render(request, 'contact.html', context)


def about(request):
    setting = Setting.objects.all()
    menu = Menu.objects.filter(status="True")
    menusearch = Menu.objects.all()
    context = {'menu': menu,
               'menusearch': menusearch,
               'setting': setting[0],
               'page': 'about',
               'pagename': 'Hakkımızda'}
    return render(request, 'about.html', context)


def referances(request):
    setting = Setting.objects.all()
    menu = Menu.objects.filter(status="True")
    menusearch = Menu.objects.all()
    context = {'menu': menu,
               'menusearch': menusearch,
               'setting': setting[0],
               'page': 'referances',
               'pagename': 'Referanslarımız'}
    return render(request, 'referances.html', context)


def academiccalendar(request):
    setting = Setting.objects.all()
    menu = Menu.objects.filter(status="True")
    menusearch = Menu.objects.all()
    context = {'menu': menu,
               'menusearch': menusearch,
               'setting': setting[0],
               'page': 'academiccalendar',
               'pagename': 'Akademik Takvim'}
    return render(request, 'academiccalendar.html', context)


def menucontent(request, id):
    try:
        content = Content.objects.get(menu_id=id)
    except:

        content = None

    if content:
        link = '/contentdetail/' + str(content.id) + '/' + content.slug
        return HttpResponseRedirect(link);
    else:
        messages.error(request, "hata ! İlgili İçerik Bulunamadı. ")
        link = '/'
        return HttpResponseRedirect(link)


def contentdetail(request, id, slug):
    setting = Setting.objects.all()
    menu = Menu.objects.filter(status="True")
    menusearch = Menu.objects.all()
    content = Content.objects.get(pk=id)
    images = Images.objects.filter(content_id=id)
    comments = Comment.objects.filter(content_id=id, status='True')
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

    context = {'menu': menu,
               'menusearch': menusearch,
               'content': content,
               'setting': setting[0],
               'page': 'contentdetail/%d/%s' % (id, slug),
               'pagename': title,
               'images': images,
               'comments': comments}
    return render(request, 'contentdetail.html', context)


def contentsearch(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            menu = Menu.objects.filter(status="True")
            menusearch = Menu.objects.all()
            query = form.cleaned_data['query']
            menuid = form.cleaned_data['menuid']
            if menuid == 0:
                contents = Content.objects.filter(title__icontains=query)
            else:
                contents = Content.objects.filter(title__icontains=query, menu_id=menuid)
            context = {'menu': menu,
                       'menusearch': menusearch,
                       'contents': contents,
                       'pagename': 'İçerik Arama', }
            return render(request, 'contentsearch.html', context)
    return HttpResponseRedirect('/')


def autosearch(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        contents = Content.objects.filter(title__icontains=q)
        results = []
        for rs in contents:
            conten_json = {}
            conten__json = rs.title.replace('<br>', '')
            results.append(conten__json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logoutview(request):
    logout(request)
    return HttpResponseRedirect('/')


def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Kullanıcı adı veya şifre hatalı. Tekrar deneyiniz.")
            return HttpResponseRedirect('/login')

    setting = Setting.objects.all()
    sliderdata = Content.objects.filter(type=4, status="True")
    newsdata = Content.objects.filter(type=2, status="True")
    announcementdata = Content.objects.filter(type=3, status="True")
    activitiesdata = Content.objects.filter(type=5, status="True")
    menu = Menu.objects.filter(status="True")
    menusearch = Menu.objects.all()
    context = {'menu': menu,
               'menusearch': menusearch,
               'setting': setting[0],
               'page': 'home',
               'sliderdata': sliderdata,
               'newsdata': newsdata,
               'announcementdata': announcementdata,
               'activitiesdata': activitiesdata}
    return render(request, 'login.html', context)


def faqs(request):
    menu = Menu.objects.filter(status="True")
    menusearch = Menu.objects.all()
    faqs = FAQ.objects.filter(status="True").order_by('ordernumber')
    context = {'menu': menu,
               'menusearch': menusearch,
               'page': 'faqs',
               'pagename': 'Sıkça Sorulan sorular',
               'faqs': faqs,
               }
    return render(request, 'faqs.html', context)
