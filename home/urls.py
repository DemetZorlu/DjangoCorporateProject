from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('referances/', views.referances, name='referances'),
    path('academiccalendar/', views.academiccalendar, name='academiccalendar'),
    path('academiccontentlist/<int:id>/<slug:slug>/', views.academiccontentlist, name='academiccontentlist'),
    path('contentdetail/<int:id>/<slug:slug>/', views.contentdetail, name='contentdetail'),

]
