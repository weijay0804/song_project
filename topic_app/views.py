from django.shortcuts import render
from django.http import HttpResponse #顯示文字 =System.out.print....
from datetime import datetime #現在時間
from django.db import connection #連接資料庫
from django.shortcuts import redirect #返回某個urls的函數

#Hello django
def sayhello(request):
    return HttpResponse("Hello Django")

#說拜拜
def bye(request):
    return HttpResponse("bye Django")

#顯示名稱+時間
def show(request,showname):
    now = datetime.now()
    return render(request, "index.html" , {"showname":showname,"now":now})

#測試 資料庫新增資料
def add_data(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("insert into topic.song(`name`,`singer`,`type`,`long`) values ('測試姥姥姥姥','謝婷之','1','250');")
        return render(request, 'index.html') #執行結束後跳回index
    

#正式程式 fight go go

#首頁
def index_start(request):
    return render(request, 'index.html') #執行結束後跳回index
