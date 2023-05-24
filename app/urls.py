# -*- coding: utf-8 -*-            
# @Time : 2023/5/21 19:19
# @name: scy
# @FileName: urls.py
# @Software: PyCharm

from django.urls import path, include
from app.views import index

urlpatterns = [
    path('', index, name='index')
]
