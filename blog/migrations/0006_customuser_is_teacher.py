# Generated by Django 2.0.13 on 2019-04-27 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_track_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_teacher',
            field=models.BooleanField(default=False, verbose_name='teacher status'),
        ),
    ]