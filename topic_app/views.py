from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect  # 顯示文字 =System.out.print....
from datetime import datetime  # 現在時間
from django.db import connection  # 連接資料庫
from django.shortcuts import redirect  # 返回某個urls的函數
from django.contrib import messages


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

        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(sn) FROM love_singer WHERE member_acc = %s", [username])

        result = cursor.fetchall()[0][0]

        if result < 3:
            content["is_first"] = True

        cursor.close()

    return render(request, 'index.html', content)  # 執行結束後跳回index


def login_view(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']

        cursor = connection.cursor()

        cursor.execute("SELECT member_acc, password FROM member WHERE member_acc=%s", (username))

        user = cursor.fetchone()

        if user is None or user[-1] != password:
            messages.info(request, "使用者或密碼輸入錯誤")

        else:
            messages.success(request, "登入成功")
            request.session["is_login"] = True
            request.session["username"] = user[0]

        cursor.close()

    return redirect("home")


def register_view(request):
    if request.method == "POST":
        username = request.POST["uname"]
        email = request.POST["email"]
        pwd = request.POST["psw"]

        cursor = connection.cursor()

        cursor.execute("SELECT member_acc FROM member WHERE member_acc = %s", [username])

        user = cursor.fetchone()

        if user:
            messages.info(request, "使用者已經存在")

        else:
            cursor.execute(
                "INSERT INTO member(member_acc, password, mail, isvip) VALUES(%s, %s, %s, %s)",
                [username, pwd, email, "1"],
            )
            messages.success(request, "註冊成功")

            request.session["is_login"] = True
            request.session["username"] = username

        cursor.close()
    return redirect("home")


def logout_view(request):
    if request.session.get("is_login"):
        request.session.flush()

    messages.success(request, "你已經登出")

    return redirect("home")
