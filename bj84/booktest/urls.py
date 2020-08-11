from django.conf.urls import url
from booktest import views


urlpatterns = [
    url(r'^index$', views.index),  # 首页
    url(r'^login$', views.login),  # 登录页面

    url(r'^login_check$', views.login_check),

    url(r'^ajax_test$', views.ajax_test),   # ajax测试界面
    url(r'^ajax_handle$', views.ajax_handle),  # ajax请求界面

    url(r'^ajax_login$', views.ajax_login),  # ajax登录页面
    url(r'^ajax_login_check$', views.ajax_login_check),  # ajax请求页面

    url(r'^set_cookie$', views.set_cookie),  # 设置cookie
    url(r'^get_cookie$', views.get_cookie),  # 获取cookie

    url(r'^set_session$', views.set_session),   # 设置session
    url(r'^get_session$', views.get_session),   # 获取session
]