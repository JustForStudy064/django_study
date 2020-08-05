from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo, HeroInfo
from django.template import loader, RequestContext


def my_render(request, template_html, context={}):
    # 使用模板文件
    # 1、加载模板文件，模板对象
    temp = loader.get_template(template_html)
    # 2、定义模板上下文，给模板文件传递数据
    context = RequestContext(request, context)
    # 3、 模板渲染:产生标准的HTML文件
    res_html = temp.render(context)
    return HttpResponse(res_html)


# Create your views here.
def index(request):
    return my_render(request, 'booktest/index.html')


def index2(request):
    return HttpResponse("老铁，没毛病")


def books(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest/books.html', {'books': books})


def detail(request, bid):
    book = BookInfo.objects.get(id=bid)
    heros = book.heroinfo_set.all()
    return render(request, 'booktest/detail.html', {'book': book, 'heros': heros})
