# -*- coding: utf-8 -*-            
# @Time : 2023/6/1 23:01
# @name: scy
# @FileName: student.py
# @Software: PyCharm

from django.urls import path, include
from app.views.student import *

urlpatterns = [
    path('login/', student_login, name='student_login'),
    path('logout/', student_logout, name='student_logout'),
    path('modify_password/', modify_password, name='student_modify_password'),
    path('get_info/', get_info, name='student_get_info'),
    path('modify_info/', modify_info, name='student_modify_info'),
    path('get_tutor/', get_tutor, name='student_get_tutor'),
    path('get_tutor_info/', get_tutor_info, name='student_get_tutor_info'),
    path('select_tutor/', select_tutor, name='student_select_tutor'),
    path('deselect_tutor/', deselect_tutor, name='student_deselect_tutor'),
    path('get_select_tutor/', get_select_tutor, name='student_get_select_tutor'),
    path('get_select_tutor_record/', get_select_tutor_record, name='student_get_select_tutor_record'),
    path('get_my_tutor/', get_my_tutor, name='student_get_my_tutor'),
]
