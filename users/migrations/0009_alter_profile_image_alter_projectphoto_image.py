# Generated by Django 4.0.5 on 2022-07-17 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_project_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='projectphoto',
            name='image',
            field=models.ImageField(default=None, upload_to='project_pics'),
        ),
    ]
