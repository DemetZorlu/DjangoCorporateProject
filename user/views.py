from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from content.models import Menu, Comment
from user.models import UserProfile, UserProfileForm


@login_required(login_url='/login')
def index(request):
    menu = Menu.objects.filter(status="True")
    menusearch = Menu.objects.all()
    profile = UserProfile.objects.get(user_id=request.user.id)
    context = {'menu': menu,
               'menusearch': menusearch,
               'page': 'user',
               'pagename': 'Kullanıcı Bilgileri',
               'profile': profile}
    return render(request, "user_profile.html", context)


@login_required(login_url='/login')
def updateuserprofile(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = UserProfile.objects.get(user_id=request.user.id)
            if not data:
                data = UserProfile()
            data.phone = form.cleaned_data['phone']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            if form.cleaned_data['image']:
                data.image = form.cleaned_data['image']
            data.save()
            messages.success(request, "Profil Bilgileriniz başarı ile güncellenmiştir.")
            return HttpResponseRedirect(url)

    messages.warning(request, "Profil Bilgileriniz güncellerken sorun ile karşılaşılmıştır. Tekrar deneyiniz.")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def updateuserpassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz değiştirilmiştir.')
            return redirect('/user')
        else:
            messages.warning(request, 'Lütfen hataları düzelterek, tekrar deneyiniz.<br>'+str(form.errors))
            return redirect('/user/updateuserpassword')
    else:
        menu = Menu.objects.filter(status="True")
        menusearch = Menu.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'updateuserpassword.html', {
            'form': form, 'menu': menu, 'menusearch': menusearch
        })

@login_required(login_url='/login')
def comments(request):
    menu = Menu.objects.filter(status="True")
    menusearch = Menu.objects.all()
    comments=Comment.objects.filter(user_id=request.user.id)
    context = {'menu': menu,
               'menusearch': menusearch,
               'page': 'user/comments',
               'pagename': 'Yorumlarım',
               'comments': comments}
    return render(request, 'user_comments.html',context)

@login_required(login_url='/login')
def deletecomment(request, id):
    Comment.objects.filter(id=id, user_id=request.user.id).delete()
    messages.success(request, 'Yorumunuz silindi.')
    return HttpResponseRedirect('/user/comments')
