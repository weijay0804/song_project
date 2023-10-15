from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.db import connection

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
        return HttpResponse('Data added successfully')