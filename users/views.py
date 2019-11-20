from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse

from common.models import Users


def index(request):
    return HttpResponse('success')


def login(request):
    # 会员登陆表单
    if request.method == 'GET':
        return render(request, 'users/login.html')
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
            # 根据账号获取登陆者的信息
            user = Users.objects.get(username=username)
            # 判断当前用户是否后台管理员用户
            if user.state == 0 or user.state == 1:
                if user.password == password:
                    # 此处登录成功，将当前登陆信息放到session中，并调转页面
                    request.session['vipuser'] = user.toDict()
                    # //todo:
                    # return redirect(reverse('index'))
                    return HttpResponse('login success')
                else:
                    context = {'info': '登陆密码错误'}
                    print(context)
            else:
                context = {'info': '此用户为非法用户'}
                print(context)
        except Exception as e:
            # print(e)
            context = {'info': '登陆账号错误:' + str(e)}
            print(context)

        return render(request, 'users/login.html', context=context)


def logout(request):
    # 会员退出
    # 清除登陆的session信息
    del request.session['vipuser']
    # 调转登录页面（url地址改变）
    return redirect(reverse('login'))


def register(request):
    # 会员注册
    if request.method == 'GET':
        return render(request, 'users/register.html')
    else:
        # 获取post提交的数据
        username = request.POST['username']
        password = request.POST['password']
        try:
            # 根据账号获取登录者信息
            user = get_object_or_404(Users, username=username)
        except Http404 as e:
            user = None
        if user:
            context = {'info':'该用户名已存在，请重新输入'}
            print(context)
            return redirect(reverse('register'))
        else:
            user = Users(username=username, password=password)
            user.save()
            request.session['vipuser'] = user.toDict()
            context = {'info' : 'success'}
            print(context)
            return redirect(reverse('login'))

