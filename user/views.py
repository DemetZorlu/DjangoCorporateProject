from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from content.models import Menu
from user.models import UserProfile


def index(request):
    menu = Menu.objects.filter(status="True")
    menusearch = Menu.objects.all()
    profile=UserProfile.objects.get(user_id=request.user.id)
    context = {'menu': menu,
               'menusearch': menusearch,
               'page': 'user',
               'pagename': 'Kullanıcı Bilgileri',
               'profile': profile}
    return render(request,"user_profile.html", context)
