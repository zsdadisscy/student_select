# -*- coding: utf-8 -*-            
# @Time : 2023/6/1 23:01
# @name: scy
# @FileName: student.py
# @Software: PyCharm

from django.urls import path, include
from app.views.student import *

urlpatterns = [
    path('login/', student_login, name='student_login'),
]
