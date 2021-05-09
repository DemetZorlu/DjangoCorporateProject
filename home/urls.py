from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('referances/', views.referances, name='referances'),
    path('academiccalendar/', views.academiccalendar, name='academiccalendar'),
    path('menucontent/<int:id>/', views.menucontent, name='menucontent'),
    path('contentdetail/<int:id>/<slug:slug>/', views.contentdetail, name='contentdetail'),
    path('search/', views.contentsearch, name='contentsearch'),
    path('autosearch/', views.autosearch, name='autosearch'),
    path('logout/', views.logoutview, name='logoutview'),
    path('login/', views.loginview, name='loginview'),
    path('faqs/', views.faqs, name='faqs'),

]
