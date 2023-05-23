from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('secondpage/',views.secondpage,name='secondpage'),
    path('secondpage/thirdpage/',views.thirdpage,name='thirdpage'),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin")

]

urlpatterns += staticfiles_urlpatterns()