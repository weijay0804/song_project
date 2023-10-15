from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

#說倪好
def sayhello(request):
    return HttpResponse("Hello Django")

#顯示名稱+時間
def show(request,showname):
    now = datetime.now()
    return render(request,"test.html",{"showname":showname,"now":now})    

# Create your views here.
