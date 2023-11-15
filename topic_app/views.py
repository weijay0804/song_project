from django.shortcuts import render
from django.http import HttpResponse  # 顯示文字 =System.out.print....
from datetime import datetime  # 現在時間
from django.db import connection  # 連接資料庫
from django.shortcuts import redirect  # 返回某個urls的函數
from .models import User


# Hello django
def sayhello(request):
    return HttpResponse("Hello Django")


# 說拜拜
def bye(request):
    return HttpResponse("bye Django")


# 顯示名稱+時間
def show(request, showname):
    now = datetime.now()
    return render(request, "index.html", {"showname": showname, "now": now})


# 測試 資料庫新增資料
def add_data(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute(
                "insert into topic.song(`name`,`singer`,`type`,`long`) values ('測試姥姥姥姥','謝婷之','1','250');"
            )
        return render(request, 'index.html')  # 執行結束後跳回index


# 正式程式 fight go go


# 首頁
def index_start(request):
    return render(request, 'index.html')  # 執行結束後跳回index


def validate_login(username, password):
    # 在這裡實現登入驗證的邏輯
    # 例如，你可以使用資料庫查詢來驗證使用者名稱和密碼

    try:
        user = User.objects.get(username=username, password=password)
        return True
    except User.DoesNotExist:
        return False


def login_view(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']

        # 下面是登入的邏輯
        authentication_successful = validate_login(username, password)

        if authentication_successful:
            return render(request, 'index.html')
        else:
            return render(request, 'index.html')
    return render(request, 'index.html')
