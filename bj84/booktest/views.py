from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def set_session(request):
    """设置session"""
    request.session['username'] = 'smart'
    request.session['age'] = 18
    return HttpResponse("设置session")


def get_session(request):
    """获取session"""
    username = request.session['username']
    age = request.session['age']
    return HttpResponse("读取session")
