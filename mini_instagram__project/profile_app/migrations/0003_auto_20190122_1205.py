# Generated by Django 2.1.5 on 2019-01-22 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0002_auto_20190121_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='desciption',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='profile_user',
            new_name='profile',
        ),
    ]
