# Generated by Django 4.2.1 on 2023-05-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0004_alter_student_photo_alter_tutor_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='id',
            field=models.PositiveIntegerField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='id',
            field=models.PositiveIntegerField(default=12, unique=True),
            preserve_default=False,
        ),
    ]
