# -*- coding: utf-8 -*-            
# @Time : 2023/6/1 23:02
# @name: scy
# @FileName: tutor.py
# @Software: PyCharm

from django.urls import path

from app.views.tutor import *

urlpatterns = [
    path('login/', tutor_login, name='tutor_login'),
    path('logout/', tutor_logout, name='tutor_logout'),
    path('modify_password/', modify_password, name='tutor_modify_password'),
    path('get_info/', get_info, name='tutor_get_info'),
    path('modify_info/', modify_info, name='tutor_modify_info'),
    path('get_student_info/', get_student_info, name='tutor_get_student_info'),
    path('get_select_student/', get_select_student, name='tutor_get_select_student'),
    path('processing_application/', processing_application, name='tutor_processing_application'),
    path('get_my_student/', get_my_student, name='tutor_get_my_student')
]
