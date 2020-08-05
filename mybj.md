## Django初学习

## 一、Django项目初体验

注意：所有条件都要保证切换到虚拟环境中，虚拟环境中的django版本是1.8.2

传统的MVC框架：

![image-20200805154918150](d:\Users\asus\Desktop\django_study\mybj.assets\image-20200805154918150.png)



​		而在Django中，则为MVT框架，不同的是，T(template)执行的是views当中的功能，而V(views)执行的是control中的功能。

#### 1.1 项目的启动:

​		在命令行中输入: django-admin startproject 项目名称

​		在命令行中输入:python manage.py startapp app的名称

​		进入到pycharm中，在settings.py中对app的名字进行注册，然后修改对应的时间:

​		UTC = 'Asia/Shanghai'

​		LANGUAGE_CODE = 'zh-hans'

​		在项目初体验当中，使用的是django设置当中的sqliteman。

#### 1.2 项目的models初体验:

​		在models当中，实现的是与数据库的交互功能，在交互功能当中，我们先建立两个表：

```python
from django.db import models

class BookInfo(models.Model):
	btitle = models.CharField(max_length=20)
	bpub_date = models.DateField()
	
	def __str__(self):
		return self.btitle
	
class HeroInfo(models.Model):
	hname = models.CharField(max_length=20)
	hgender = models.BooleanField(default=False)
	hcomment = models.CharField(max_length=20)
	hbook = models.ForeignKey(BookInfo)
	
	def __str__(self):
		return self.hname
```

​		在这里，建立了两个表，分别是图书表和英雄表，在两个表中，分别使用到了**__str__**魔法方法，这在之后的admin界面中会有用。

​		建立好表之后，需要在命令行中执行以下两行代码：

```
	python manage.py makemigrations
	python manage.py migrate
```

​		对表进行迁移之后，会自动生成migrations文件。

​		之后再执行

```
	python manage.py shell
```

​		然后在shell中可以对表中的内容进行操作，进行存取，在之后的models部分会详细地说明

#### 1.3 项目中的admin.py

​		我们通常需要进入后台，对数据库中的表格进行操作，这时候，如果我们能有一个交互界面可以直接进行表格数据的操作，会更加舒服，这时候就需要用到admin.py

​		在admin.py中进行注册：

```python
from django.contrib import admin
from booktest.models import BookInfo,HeroInfo

admin.site.register(BookInfo)
admin.site.register(HeroInf0)
```

​		之后运行: 

```
python manage.py createsuperuser
```

​		按照相应的步骤创建超级管理员，然后进入 **127.0.0.1::8000/admin**  后台管理页面，输入相应的账号和密码，即可进入相应的页面，可以对数据库中的表格进行操作。

#### 1.4 项目中的views.py

​		在django的views中，负责的是MVT当中的V功能，相当于MVC中的控制器，这时候需要对urls.py进行配置：

​		在views.py中，进行页面的注册:

```python
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello python")

def index2(request):
	return HttpResponse("老铁，没毛病")
```

​		在对应的app中，建立urls.py

![image-20200805161055044](d:\Users\asus\Desktop\django_study\mybj.assets\image-20200805161055044.png)



​		在新建立的urls.py中进行配置：

```python
from django.conf.urls import url
from booktest import views

# 利用正则表达式对view中对应的视图函数进行严格匹配
urlpatterns = [
    url(r'^index$',views.index)
    url(r'^index2$',views.index2)
]
```

​		在原有的urls.py文件中注册app中的urls.py

```python
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    
    # 其他都是原有的，下一行才是注册
    url(r'^', include('booktest.urls'))
]
```

​		再次运行python manage.py runserver ， 输入**127.0.0.1/index **和**127.0.0.1/index2 ** 可以看到，返回的HttpResponse被成功地返回到页面上

#### 1.5 template初体验

​		在之前的index当中，仅仅只返回了一句简单的问候语，如果想要返回一个完整的HTML页面，还要在template当中进行页面的调整。

​		在对应的项目目录中，创建一个templates文件，并且在settings.py中进行配置。

![image-20200805164340819](d:\Users\asus\Desktop\django_study\mybj.assets\image-20200805164340819.png)

![image-20200805164357122](d:\Users\asus\Desktop\django_study\mybj.assets\image-20200805164357122.png)

​		这样就实现了对templates的注册，在对应的app中进行views.py的配置:

```python
from django.shortcuts import render
form django.http import HttpResponse
from django.template import loader,RequestContext

# 注册的过程往往有三步:
def index(request):
    # 使用模板文件:
   	# 1、加载模板文件(这里会根据settings.py当中的相关参数进行拼接)
    temp = loader.get_template('booktest/index.html')
    # 2、定义模板上下文，给模板文件传递数据
    context = RequestContext(request, context)
    # 3、模板渲染，产生标准的HTML页面
    res_html = temp.loader(context)
    return HttpResponse(res_html)

def index(request):
    return render(requset,'booktest/index.html',{})
```

​		在使用模板文件的时候，通常需要三步：分别是(1) 加载模板文件；(2) 定义模板上下文，给模板文件传递数据; (3)模板渲染，产生标准的HTML页面，由于每次在使用模板的时候都需要经过这三步，这时候我们可以考虑把它封装成一个函数，而在django.shortcuts 当中，已经写好了render函数，我们只需要直接使用即可，如index2当中的内容，在之后，会对模板文件进行进一步的探讨。



#### 1.6 进行案例的简单设计(作业)

​		在案例当中，需要用到一点template当中的知识。

​		需求:

编码之前的准备工作：

1) 设计出访问页面的url和对应的视图函数的名字，确定视图函数的功能。

2) 设计模板文件的名字。

***\*以下为案例中的简单设计过程：\****

1) 完成图书信息的展示：

a) 设计url，通过浏览器访问 [http://127.0.0.1:8000/books 时显示图书信息页面](http://127.0.0.1:8000/books/ 时显示图书信息页面)。

b) 设计url对应的视图函数show_books。

查询出所有图书的信息，将这些信息传递给模板文件。

c) 编写模板文件show_books.html。

遍历显示出每一本图书的信息。

2) 完成点击某本图书时，显示出图书里所有英雄信息的页面。

a) 设计url,通过访问http://127.0.0.1:8000/books/数字时显示对应的英雄信息页面。

这里数字指点击的图书的id。

b) 设计对应的视图函数detail。

​			接收图书的id,根据id查询出相应的图书信息，然后查询出图书中的所有英雄信息。

c) 编写模板文件detail.html。