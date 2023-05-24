from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import Group, Permission


# 将权限删除，后期可拓展
class Tutor(AbstractBaseUser):
    username = models.CharField('姓名', max_length=10, blank=True)
    id = models.CharField('工号', max_length=10, primary_key=True)
    USERNAME_FIELD = 'id'
    date_of_birth = models.DateField('出生日期')
    gender = models.CharField('性别', max_length=10, choices=[('man', '男'), ('women', '女')], default='man')
    email = models.EmailField('邮箱', blank=False)
    phone = models.CharField('手机号', max_length=20, blank=False)
    research_area = models.CharField('研究方向', max_length=100)
    bio = models.TextField('简介')
    is_recruiting = models.BooleanField('是否招收学生', default=False, blank=False)
    enrollment_type = models.CharField('招生类型', max_length=50,
                                       choices=[('special_master', '专硕'), ('learning_master', '学硕')])
    enrollment_limit = models.PositiveIntegerField('招生上限', default=0)
    enrollment_count = models.PositiveIntegerField('目前招生', default=0)

    # groups = models.ManyToManyField(Group, related_name='%(class)s_groups')
    # user_permissions = models.ManyToManyField(Permission, related_name='%(class)s_user_permissions')
    photo = models.ImageField('头像', upload_to='tutor_photo/', default='tutor_photo/tutor_photo.png')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '导师'
        verbose_name_plural = '导师'


class Student(AbstractBaseUser):
    username = models.CharField('姓名', max_length=10, blank=True)
    id = models.CharField('学号', max_length=10, primary_key=True)
    date_of_birth = models.DateField('出生日期')
    gender = models.CharField('性别', max_length=10, choices=[('man', '男'), ('women', '女')], default='man')
    student_type = models.CharField('学生类型', max_length=50,
                                    choices=[('special_master', '专硕'), ('learning_master', '学硕')],
                                    default='special_master')
    bio = models.TextField('简介')
    email = models.EmailField('邮箱', blank=False)
    phone = models.CharField('手机号', max_length=20, blank=False)
    is_selected = models.BooleanField('是否有老师选择', default=False)
    select_limit = models.PositiveIntegerField('选择老师上线', default=0)
    select_count = models.PositiveIntegerField('目前已选择的老师数目', default=0)
    # groups = models.ManyToManyField(Group, related_name='%(class)s_groups')
    # user_permissions = models.ManyToManyField(Permission, related_name='%(class)s_user_permissions')
    photo = models.ImageField('头像', upload_to='student_photo/', default='student_photo/student_photo.png')
    USERNAME_FIELD = 'id'
    selected_tutor = models.ForeignKey('Tutor', verbose_name='导师', related_name='tutor_student',
                                       on_delete=models.CASCADE, null=True,
                                       blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'


class StudentTeacher(models.Model):
    student = models.ForeignKey('Student', verbose_name='学生', on_delete=models.CASCADE, related_name='tutor')
    tutor = models.ForeignKey('Tutor', on_delete=models.CASCADE, verbose_name='导师', related_name='student')
    relationship_status = models.CharField('状态', max_length=20,
                                           choices=[('accepted', '已接受'), ('rejected', '已拒绝'),
                                                    ('pending', '待定')], default='pending')

    class Meta:
        index_together = (('student', 'tutor'),)  # 如果需要支持组合查询，可以添加多个外键到Meta类中
        unique_together = (('student', 'tutor'),)  # 如果需要支持唯一性约束，可以添加多个字段到unique_together类中
        verbose_name = '学生选择的导师'
        verbose_name_plural = '学生选择的导师'

    def __str__(self):
        return f"{self.student.username} - {self.tutor.username}"


class UserLog(models.Model):
    student = models.ForeignKey('Student', verbose_name='学生', on_delete=models.CASCADE, related_name='student_logs')
    tutor = models.ForeignKey('Tutor', verbose_name='导师', on_delete=models.CASCADE, related_name='tutor_logs')
    operation_type = models.CharField(
        '操作类型',
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

    class Meta:
        verbose_name = '学生选择记录'
        verbose_name_plural = '学生选择记录'
