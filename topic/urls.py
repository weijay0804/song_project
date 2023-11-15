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
from django.urls import path, re_path
from topic_app.views import sayhello, show, bye, add_data, index_start
from topic_app.views import login_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index", sayhello),  # 跳Hello django
    path("bye", bye),  # 說拜拜
    re_path(r'^show/(\w+)/$', show, name="show"),
    path('add_data', add_data, name='add_data'),
    # 正式程式 fighting
    path("", index_start),  # 說拜拜
    path('login/', login_view, name='login'),  # 定義一個 URL 路徑 '/login/'
]
