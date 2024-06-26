# -*- coding: utf-8 -*-            
# @Time : 2023/6/1 23:01
# @name: scy
# @FileName: __init__.py.py
# @Software: PyCharm

from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def get_home(request):
    return render(request, 'index.html')


def get_cache(request):
    if request.method == 'GET':
        user = request.GET.get('user')
    elif request.method == 'POST':
        user = request.POST.get('user')
    else:
        return False, ''
    return cache.has_key(user), user


def update_cache(request):
    flag, user = get_cache(request)
    if not flag:
        return
    cache.set(user, cache.get(user), 3600 * 24)


@require_http_methods(["GET"])
def get_status(request):
    flag, user = get_cache(request)
    if not flag:
        return JsonResponse({
            'result': '未登录',
        })
    return JsonResponse({
        'result': cache.get(user)[1],
    })
