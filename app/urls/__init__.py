# -*- coding: utf-8 -*-            
# @Time : 2023/6/1 23:00
# @name: scy
# @FileName: __init__.py
# @Software: PyCharm

from django.urls import path, include

from app.views import *

urlpatterns = [
    # path('', index, name='index')
    path('student/', include('app.urls.student')),
    path('tutor/', include('app.urls.tutor')),
    path('get_status/', get_status, name='get_satus')
]
