# Generated by Django 4.0.5 on 2022-06-24 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_project_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(blank=True, default=None, max_length=1000)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_videos', to='users.project')),
            ],
        ),
    ]
