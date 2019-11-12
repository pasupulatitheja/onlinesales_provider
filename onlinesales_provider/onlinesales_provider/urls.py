"""onlinesales_provider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showlogin,name="login"),
    path('index/',views.showindex,name="index"),
    path('add/',views.randamid_pass,name="add"),
    path('savemerchant/',views.savemerchant,name="savemerchant"),
    path("viewmerchant/",views.viewmerchant,name="viewmerchant"),
    path('delete/',views.deletemerchant,name="delete"),
    path('checkuser/<str:username>/<str:password>/',views.checkuser.as_view()),
    path('resertpassword/<str:gmailusername>/',views.resertpassword.as_view()),
    path('changepassword/<str:email>/<str:password>/',views.changepassword.as_view()),
    path('savedata/',views.showsavedata.as_view()),
    path('showproduct/',views.showproduct.as_view()),
    path('providerdelete/<int:id>/',views.showproviderdelete)



]
