"""
URL configuration for django_study project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
    路由的类型
        1.普通路由
        
        2.动态路由(参数路由)
            path('detail/<type:key>')参数的占位符如果不设置转换类型，默认为字符串str类型
            路由参数转换器：Django默认提供了一些路由参数转换器：int, str, slug, uuid, path,(在django.urls.converters.py)
            动态路由参数类型
            django
                int：限定参数类型为整形
                str:限定参数类型为字符串，但字符串中不能包含'/'
                uuid:限定参数类型为uuid(8-4-4-4-12)
                slug:限定参数类型为slug,匹配字母，数组，下划线，中划线组成的字符串
                path：限定参数类型为路径，可以包含'/',匹配任意字符串        
        3.正则路由
            
            > 路由的地址支持正则表达式, 需要使用 re_path
        4.分布式路由
path 函数
# 前两个为必填参数
def _path(route, view, kwargs=None, name=None, Pattern=None):
    from django.views import View
    > route : 设置 路由地址， 
    > view : 设置视图函数 该路由对应的 执行程序
    > kwargs : 是一个字典格式的数据， 给路由对应的视图函数view 设置 额外的参数
    > name : 设置路由名称

"""



from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 定义一个路由 用来访问 登录
    path('login', views.login, name="login"),

    path("detail/<int:id>", views.detail, name="detail"),
    # re_path 正则路由 路由名为一个正则表达式匹配 匹配前要加r("^$")代表不匹配任何内容
    re_path(r"^$",  views.index, name="index")

]
