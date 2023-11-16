from django.shortcuts import render
from django.shortcuts import redirect  # 返回某個urls的函數
from django.contrib import messages

from . import crud


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

        love_relation_singer = crud.get_relation_singer(username)

        content["love_relation_singer"] = love_relation_singer

        user_song_list = crud.get_song_list(username)
        content["song_list"] = user_song_list

        user_sound_list = crud.get_user_sound(username)
        content["sound_list"] = user_sound_list

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
