# Generated by Django 4.0.5 on 2022-06-24 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_project_video_projectphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='video',
        ),
    ]
