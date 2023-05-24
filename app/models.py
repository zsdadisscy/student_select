from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import Group, Permission


class Student(AbstractUser, PermissionsMixin):
    student_id = models.CharField(max_length=10, primary_key=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    student_type = models.CharField(max_length=50)
    bio = models.TextField()
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=20, blank=False)
    is_selected = models.BooleanField(default=False)
    select_limit = models.PositiveIntegerField(default=0)
    select_count = models.PositiveIntegerField(default=0)
    groups = models.ManyToManyField(Group, related_name='%(class)s_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='%(class)s_user_permissions')
    photo = models.ImageField(upload_to='student_photo/', default='student_photo/student_photo.png')

    def __str__(self):
        return self.username


class Tutor(AbstractUser, PermissionsMixin):
    employee_id = models.CharField(max_length=10, primary_key=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=20, blank=False)
    research_area = models.CharField(max_length=100)
    bio = models.TextField()
    is_recruiting = models.BooleanField(default=False, blank=False)
    enrollment_type = models.CharField(max_length=50)
    enrollment_limit = models.PositiveIntegerField(default=0)
    enrollment_count = models.PositiveIntegerField(default=0)
    selected_students = models.ForeignKey('Student', related_name='tutor_student', on_delete=models.CASCADE, null=True,
                                          blank=True)
    groups = models.ManyToManyField(Group, related_name='%(class)s_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='%(class)s_user_permissions')
    photo = models.ImageField(upload_to='tutor_photo/', default='tutor_photo/tutor_photo.png')

    def __str__(self):
        return self.username


class StudentTeacher(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='tutor')
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE, related_name='student')
    relationship_status = models.CharField(max_length=20, choices=[('accepted', '已接受'), ('rejected', '已拒绝'),
                                                                   ('pending', '待定')], default='pending')

    class Meta:
        index_together = (('student', 'tutor'),)  # 如果需要支持组合查询，可以添加多个外键到Meta类中
        unique_together = (('student', 'tutor'),)  # 如果需要支持唯一性约束，可以添加多个字段到unique_together类中

    def __str__(self):
        return f"{self.student.username} - {self.tutor.username}"


class UserLog(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='student_logs')
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE, related_name='tutor_logs')
    operation_type = models.CharField(
        max_length=20,
        choices=(
            ('choose', '选择导师'),
            ('cancel', '取消选择'),
            ('approve', '导师通过'),
            ('reject', '导师拒绝'),
        )
    )
    operation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.tutor} - {self.operation_type} - {self.operation_time}"
