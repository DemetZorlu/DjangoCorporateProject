from django.urls import path

from user import views

urlpatterns = [
    path('', views.index, name='index'),
    path('updateuserprofile/', views.updateuserprofile, name="updateuserprofile"),
    path('updateuserpassword/', views.updateuserpassword, name="updateuserpassword"),
    path('comments/', views.comments, name="comments"),
    path('deletecomment/<int:id>',views.deletecomment, name='deletecomment'),
    path('addcontent/', views.addcontent, name='addcontent'),
    path('contents/', views.contents, name='contents'),
    path('contentedit/<int:id>', views.contentedit, name='contentedit'),
    path('contentdelete/<int:id>', views.contentdelete, name='contentdelete'),
]
