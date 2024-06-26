# Generated by Django 4.2.1 on 2023-06-19 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=10, verbose_name='姓名')),
                ('password', models.CharField(default='pbkdf2_sha256$600000$qKnEGwhvpDvbtIB5F4oisv$kOPYIzplMXi+E2d25vmyZIf365CpNKAKztgu58KjTPY=', max_length=250, verbose_name='密码')),
                ('college', models.CharField(choices=[('college_of_computer', '计算机学院'), ('engineering_college', '工学院'), ('school_of_media', '传媒学院'), ('academy_of_fine_arts', '美术学院'), ('conservatory_of_music', '音乐学院')], default='计算机学院', max_length=50, verbose_name='学院')),
                ('id', models.CharField(default='123456', max_length=10, primary_key=True, serialize=False, verbose_name='学号')),
                ('date_of_birth', models.DateField(verbose_name='出生日期')),
                ('gender', models.CharField(choices=[('man', '男'), ('women', '女')], default='man', max_length=10, verbose_name='性别')),
                ('student_type', models.CharField(choices=[('special_master', '专硕'), ('learning_master', '学硕')], default='special_master', max_length=50, verbose_name='学生类型')),
                ('bio', models.TextField(verbose_name='简介')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=20, verbose_name='手机号')),
                ('is_selected', models.BooleanField(default=False, verbose_name='是否有老师选择')),
                ('select_limit', models.PositiveIntegerField(default=5, verbose_name='选择老师上限')),
                ('select_count', models.PositiveIntegerField(default=0, verbose_name='目前已选择的老师数目')),
                ('photo', models.ImageField(default='student_photo/student_photo.png', upload_to='student_photo/', verbose_name='头像')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=10, verbose_name='姓名')),
                ('password', models.CharField(default='pbkdf2_sha256$600000$rLIq0miJHZjLijLjh9vHrr$VREH+ECcjxh9P6/LX5ahpvbDkANGIOob1qWNt4OV+j4=', max_length=250, verbose_name='密码')),
                ('id', models.CharField(default='123456', max_length=10, primary_key=True, serialize=False, verbose_name='工号')),
                ('date_of_birth', models.DateField(verbose_name='出生日期')),
                ('college', models.CharField(choices=[('college_of_computer', '计算机学院'), ('engineering_college', '工学院'), ('school_of_media', '传媒学院'), ('academy_of_fine_arts', '美术学院'), ('conservatory_of_music', '音乐学院')], default='计算机学院', max_length=50, verbose_name='学院')),
                ('gender', models.CharField(choices=[('man', '男'), ('women', '女')], default='man', max_length=10, verbose_name='性别')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=20, verbose_name='手机号')),
                ('research_area', models.CharField(max_length=100, verbose_name='研究方向')),
                ('bio', models.TextField(verbose_name='简介')),
                ('is_recruiting_specialized', models.BooleanField(default=False, verbose_name='是否招收专硕学生')),
                ('is_recruiting_learning', models.BooleanField(default=False, verbose_name='是否招收学硕学生')),
                ('enrollment_limit', models.PositiveIntegerField(default=5, verbose_name='招生上限')),
                ('enrollment_count', models.PositiveIntegerField(default=0, verbose_name='目前招生')),
                ('photo', models.ImageField(default='tutor_photo/tutor_photo.png', upload_to='tutor_photo/', verbose_name='头像')),
            ],
            options={
                'verbose_name': '导师',
                'verbose_name_plural': '导师',
            },
        ),
        migrations.CreateModel(
            name='StudentLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_type', models.CharField(choices=[('choose', '选择导师'), ('cancel', '取消选择'), ('approve', '导师通过'), ('reject', '导师拒绝')], max_length=20, verbose_name='操作类型')),
                ('operation_time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_logs', to='app.student', verbose_name='学生')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_logs', to='app.tutor', verbose_name='导师')),
            ],
            options={
                'verbose_name': '操作记录',
                'verbose_name_plural': '操作记录',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='selected_tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_student', to='app.tutor', verbose_name='导师'),
        ),
        migrations.CreateModel(
            name='StudentTutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship_status', models.CharField(choices=[('accepted', '已接受'), ('rejected', '已拒绝'), ('pending', '待定')], default='pending', max_length=20, verbose_name='状态')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to='app.student', verbose_name='学生')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='app.tutor', verbose_name='导师')),
            ],
            options={
                'verbose_name': '学生选择的导师',
                'verbose_name_plural': '学生选择的导师',
                'unique_together': {('student', 'tutor')},
                'index_together': {('student', 'tutor')},
            },
        ),
    ]
