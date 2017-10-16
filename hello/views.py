# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from hello import models

# Create your views here.
from django.shortcuts import HttpResponse


def index(request):
    if request.method=="POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.UserInfo.objects.create(user=username, pwd=password)
        #添加数据到数据库，从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data": user_list})
    #return HttpResponse("hello world")

