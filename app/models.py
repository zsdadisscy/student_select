from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from django.contrib.auth.models import Group, Permission
from django.db import models


class TutorManager(BaseUserManager):
    def create_user(self, id, password=None, **extra_fields):
        user = self.model(id=id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(id, password, **extra_fields)

    def create(self, **param):
        return self.create_user(**param)


# 将权限删除，后期可拓展
class Tutor(AbstractBaseUser):
    username = models.CharField('姓名', max_length=10, blank=False)
    password = models.CharField('密码', max_length=250, default=make_password('123456'))
    id = models.CharField('工号', max_length=10, primary_key=True, null=False, default='123456')
    USERNAME_FIELD = 'id'
    date_of_birth = models.DateField('出生日期')
    college = models.CharField('学院', max_length=50, blank=False,
                               choices=[('college_of_computer', '计算机学院'), ('engineering_college', '工学院'),
                                        ('school_of_media', '传媒学院'), ('academy_of_fine_arts', '美术学院'),
                                        ('conservatory_of_music', '音乐学院')], default='计算机学院')
    gender = models.CharField('性别', max_length=10, choices=[('man', '男'), ('women', '女')], default='man')
    email = models.EmailField('邮箱', blank=False)
    phone = models.CharField('手机号', max_length=20, blank=False)
    research_area = models.CharField('研究方向', max_length=100)
    bio = models.TextField('简介')
    is_recruiting_specialized = models.BooleanField('是否招收专硕学生', default=False, blank=False)
    is_recruiting_learning = models.BooleanField('是否招收学硕学生', default=False, blank=False)
    enrollment_limit = models.PositiveIntegerField('招生上限', default=5)
    enrollment_count = models.PositiveIntegerField('目前招生', default=0)
    photo = models.ImageField('头像', upload_to='tutor_photo/', default='tutor_photo/tutor_photo.png')

    objects = TutorManager()

    def __str__(self):
        return f"{self.username} - {self.id}"

    class Meta:
        verbose_name = '导师'
        verbose_name_plural = '导师'


class StudentManager(BaseUserManager):
    def create_user(self, id, password=None, **extra_fields):
        user = self.model(id=id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(id, password, **extra_fields)

    def create(self, **param):
        return self.create_user(**param)


class Student(AbstractBaseUser):
    username = models.CharField('姓名', max_length=10, blank=False)
    password = models.CharField('密码', max_length=250, default=make_password('123456'))
    college = models.CharField('学院', max_length=50, blank=False,
                               choices=[('college_of_computer', '计算机学院'), ('engineering_college', '工学院'),
                                        ('school_of_media', '传媒学院'), ('academy_of_fine_arts', '美术学院'),
                                        ('conservatory_of_music', '音乐学院')], default='计算机学院')
    id = models.CharField('学号', max_length=10, primary_key=True, null=False, default='123456')
    date_of_birth = models.DateField('出生日期')
    gender = models.CharField('性别', max_length=10, choices=[('man', '男'), ('women', '女')], default='man')
    student_type = models.CharField('学生类型', max_length=50,
                                    choices=[('special_master', '专硕'), ('learning_master', '学硕')],
                                    default='special_master')
    bio = models.TextField('简介')
    email = models.EmailField('邮箱', blank=False)
    phone = models.CharField('手机号', max_length=20, blank=False)
    is_selected = models.BooleanField('是否有老师选择', default=False)
    select_limit = models.PositiveIntegerField('选择老师上限', default=5)
    select_count = models.PositiveIntegerField('目前已选择的老师数目', default=0)
    USERNAME_FIELD = 'id'
    selected_tutor = models.ForeignKey('Tutor', verbose_name='导师', related_name='tutor_student',
                                       on_delete=models.CASCADE, null=True,
                                       blank=True)
    photo = models.ImageField('头像', upload_to='student_photo/', default='student_photo/student_photo.png')
    objects = StudentManager

    def __str__(self):
        return f"{self.username} - {self.id}"

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'


class StudentTutor(models.Model):
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


class StudentLog(models.Model):
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
    operation_time = models.DateTimeField('操作时间', auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.tutor} - {self.operation_type} - {self.operation_time}"

    class Meta:
        verbose_name = '操作记录'
        verbose_name_plural = '操作记录'
