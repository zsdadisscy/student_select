from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import *


# Register your models here.



admin.site.site_header = '硕士导师双选系统后台管理'
admin.site.index_title = '后台管理'
admin.site.site_title = '后台管理'

admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(StudentTeacher)
admin.site.register(UserLog)
