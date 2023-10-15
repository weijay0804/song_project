from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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
