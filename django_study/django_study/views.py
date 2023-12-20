from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render, redirect

def index(request):
    # 重定向 是页面进行跳转的 重要反式之一
    # 1)  是两次起请求， 第一次请求 会向浏览器 返回  一个301/302状态码 并返回location特殊头信息
    # 2） 地址栏的 请求地址 发生了改变
    # 3） 重定向 不能通过 request 携带数据到 网页中
    # 4） 重定向 可以 跳转到任意网址中

    return redirect(to="detail",id=999)

def login(request):
    return render(request, "login.html")


def detail(request, id):
    return render(request, "detail.html", locals())

# def index(request):
#     # 返回一个JSON
#     # data = [
#     # {"name": "张三", "sex":"男", "age": 20},
#     # {"name": "李四", "sex":"男", "age": 20},
#     # {"name": "王五", "sex":"男", "age": 20},
#     # ]
#     # HttpResponse 是最强大的响应对象，可以设置响应头，响应状态码，响应体等 render, JsonResponse, FileResponse 等都是基于HttpResponse
#     # return HttpResponse(data)
#     # rb r 代表read b 代表binary（二进制形式） 代表以二进制形式读  wb w write 代表以二进制形式写
#     with open("1.webp", "rb") as f:
#         data = f.read()
#         # content 内容  content_type 内容类型image/jpeg以图片形式打开
#         return HttpResponse(content=data,
#                             content_type="image/jpeg"
#                             )
#
#
#     #  这种形式打开文件 要自己关闭
#     # f = open("","rb")
#     # f.close()