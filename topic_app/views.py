from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect  # 顯示文字 =System.out.print....
from datetime import datetime  # 現在時間
from django.db import connection  # 連接資料庫
from django.shortcuts import redirect  # 返回某個urls的函數
from django.contrib import messages

from . import crud


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
    content = {}

    if request.session.get("is_login"):
        content["is_login"] = True
        content["username"] = request.session.get("username")

        username = request.session["username"]

        user_love_singer_num = crud.count_user_love_singers(username)

        if user_love_singer_num < 3:
            content["is_first"] = True

            singers = crud.get_singers()
            singers = [s[0] for s in singers]
            content["singers"] = singers

    return render(request, 'index.html', content)  # 執行結束後跳回index


def add_favorites_singer_view(requset):
    if requset.method == "POST":
        if not requset.session.get("is_login"):
            messages.info(requset, "請先登入")
            return redirect("home")

        select = requset.POST.getlist('favorite_singers_select', [])

        username = requset.session.get("username")

        crud.add_user_love_singer(select, username)

        messages.success(requset, "新增成功")

    return redirect("home")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']

        user_data = crud.get_user(username)

        if user_data is None or user_data["password"] != password:
            messages.info(request, "使用者或密碼輸入錯誤")

        else:
            messages.success(request, "登入成功")
            request.session["is_login"] = True
            request.session["username"] = user_data["member_acc"]

    return redirect("home")


def register_view(request):
    if request.method == "POST":
        username = request.POST["uname"]
        email = request.POST["email"]
        pwd = request.POST["psw"]

        user_data = crud.get_user(username)

        if user_data:
            messages.info(request, "使用者已經存在")

        else:
            crud.add_user(username, pwd, email)
            messages.success(request, "註冊成功")

            request.session["is_login"] = True
            request.session["username"] = username

    return redirect("home")


def logout_view(request):
    if request.session.get("is_login"):
        request.session.flush()

    messages.success(request, "你已經登出")

    return redirect("home")
