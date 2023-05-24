from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import *


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'gender', 'email', 'phone', 'date_of_birth', 'student_type')


class TutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'gender', 'email', 'phone', 'date_of_birth')


admin.site.site_header = '硕士导师双选系统后台管理'
admin.site.index_title = '后台管理'
admin.site.site_title = '后台管理'

admin.site.register(Student, StudentAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(StudentTeacher)
admin.site.register(UserLog)
