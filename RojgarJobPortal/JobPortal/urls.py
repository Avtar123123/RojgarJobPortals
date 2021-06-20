from django.urls import path
from django.contrib import admin
from . import views
admin.site.site_title='Rojgar Job Portal'
admin.site.site_header='IT job Portal'
admin.site.index_title='Online job portal'
urlpatterns = [
    path('',views.hom,name='hom'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerUser,name='register'),
    path('apply/',views.applyPage,name='apply'),
     path('applied/',views.applied,name='applied'),
    path('home' , views.home , name="home"),
   path('view_score' , views.view_score , name="view_score"),
   path('api/check_score' , views.check_score , name="check_score"),
   path('<id>' , views.take_quiz , name="take_quiz"),
   path('api/<id>' , views.api_question, name="api_question"),
]