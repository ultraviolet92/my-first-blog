# Generated by Django 2.0.13 on 2019-04-07 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_student',
            field=models.BooleanField(default=False, verbose_name='student_status'),
        ),
    ]