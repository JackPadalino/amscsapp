# Generated by Django 4.0.5 on 2022-07-16 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_project_classroom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='classroom',
        ),
    ]
