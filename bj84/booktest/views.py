from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta


# Create your views here.
def index(request):
    return render(request, 'booktest/index.html', {})


def login(request):
    return render(request, 'booktest/login.html', {})


def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    if (username == 'admin'):
        if (password == '123456'):
            print("登录成功!")
            if (remember == 'on'):
                r = redirect('/index')
                r.set_cookie('username', username, max_age=3 * 3600)
                r.set_cookie('password', password, max_age=3 * 3600)
                return r
            else:
                return redirect("/index")
        else:
            print("密码错误")
    else:
        print("用户名错误")
    return redirect('/login')


def ajax_test(request):
    """返回一个ajax页面"""
    return render(request, 'booktest/ajax_test.html', {})


def ajax_handle(request):
    return JsonResponse({'res': 1})


def ajax_login(request):
    return render(request, 'booktest/ajax_login.html')


def ajax_login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(request)
    if (username == 'admin'):
        if (password == '123456'):
            return JsonResponse({'res': 1})
        else:
            return JsonResponse({'res': 0})
    else:
        return JsonResponse({'res': 0})


def set_cookie(request):
    """设置cookie"""
    response = HttpResponse('设置cookie')
    # 设置一个cookie信息，键为num，值为1，max_age设置的是过期的秒数(2周)
    response.set_cookie('num', 1, max_age=14 * 24 * 3600)
    response.set_cookie('num2', 1, expires=datetime.now() + timedelta(days=14))
    return response


def get_cookie(request):
    num = request.COOKIES['num']
    num2 = request.COOKIES['num2']
    return HttpResponse(num + num2)


def set_session(request):
    request.session['username'] = 'admin'
    request.session['password'] = '123456'
    return HttpResponse('设置session')


def get_session(request):
    """获取session"""
    username = request.session['username']
    password = request.session['password']
    return HttpResponse(username + ' ' + password)
