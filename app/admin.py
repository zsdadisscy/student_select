from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import *


# Register your models here.
class StudentAdmin(UserAdmin):
    model = Student
    list_display = ('username', 'email', 'student_id', 'date_of_birth', 'gender', 'student_type')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(is_superuser=False)  # 只显示非超级用户
        return queryset

    def get_user_type(self, obj):
        return 'Student'

    get_user_type.short_description = 'User Type'


class TutorAdmin(UserAdmin):
    model = Tutor
    list_display = ('username', 'email', 'employee_id', 'date_of_birth', 'gender', 'research_area')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(is_superuser=False)  # 只显示非超级用户
        return queryset

    def get_user_type(self, obj):
        return 'Tutor'

    get_user_type.short_description = 'User Type'


admin.site.site_header = 'Custom Admin Panel'
admin.site.index_title = 'Custom Dashboard'
admin.site.register(Student, StudentAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(StudentTeacher)
admin.site.register(UserLog)
