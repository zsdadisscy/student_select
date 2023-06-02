# -*- coding: utf-8 -*-            
# @Time : 2023/6/1 23:04
# @name: scy
# @FileName: student.py
# @Software: PyCharm

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.views.decorators.http import require_http_methods

from app.models import Student


@require_http_methods(["POST"])
def student_login(request):
    data = request.POST
    id = data.get('id')
    password = data.get('password')
    if not id:
        return JsonResponse({
            'result': '学号不能为空'
        })
    if not password:
        return JsonResponse({
            'result': '密码不能为空'
        })
    # 初始密码不加密
    if password != '123456':
        password = make_password(password)
    try:
        user = Student.objects.get(id=id)
        if user.password != password:
            return JsonResponse({
                'result': '密码不正确'
            })
        login(request, user)
        return JsonResponse({
            'result': 'success'
        })
    except Student.DoesNotExist:
        return JsonResponse({
            'result': '用户不存在',
        })

