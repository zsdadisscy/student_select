from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import *


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'gender', 'email', 'phone', 'date_of_birth', 'student_type', 'college')
    exclude = ('password',)
    search_fields = ('id',)


class TutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'gender', 'email', 'phone', 'date_of_birth', 'college')
    exclude = ('password',)
    search_fields = ('id',)


class StudentTutorAdmin(admin.ModelAdmin):
    list_display = ('student', 'tutor', 'relationship_status')


class StudentLogAdmin(admin.ModelAdmin):
    list_display = ('student', 'tutor', 'operation_type', 'operation_time')
    readonly_fields = ('operation_time',)


admin.site.site_header = '硕士导师双选系统后台管理'
admin.site.index_title = '后台管理'
admin.site.site_title = '后台管理'

admin.site.register(Student, StudentAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(StudentTutor, StudentTutorAdmin)
admin.site.register(StudentLog, StudentLogAdmin)
