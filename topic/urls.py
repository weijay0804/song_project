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

from django.urls import path
from topic_app.views import (
    login_view,
    logout_view,
    register_view,
    add_favorites_singer_view,
    index_start,
)

urlpatterns = [
    # 正式程式 fighting
    path("", index_start, name="home"),  # 說拜拜
    path('login/', login_view, name='login'),  # 定義一個 URL 路徑 '/login/'
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("add_favorites_singer/", add_favorites_singer_view, name="add_favorites_singer"),
]
