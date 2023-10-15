"""topic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,re_path
from topic_app.views import sayhello,bye, sayhello2,index

urlpatterns = [
    path("admin/", admin.site.urls),

    path("index",sayhello), # 跳Hello django

    path("bye",bye), # 說拜拜

    re_path(r'^sayhello/(\w+)/$', sayhello2, name='sayhello2'),

    re_path(r'^index/(\w+)/$', index, name='index'),

]
