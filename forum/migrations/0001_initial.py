# Generated by Django 4.0.5 on 2022-06-29 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='classroom.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='forum.forum')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('project_link', models.CharField(blank=True, default=None, max_length=1000)),
                ('image', models.ImageField(blank=True, default=None, upload_to='')),
                ('video', models.CharField(blank=True, default=None, max_length=1000)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='forum.forum')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='forum.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('project_link', models.CharField(blank=True, default=None, max_length=1000)),
                ('image', models.ImageField(blank=True, default=None, upload_to='')),
                ('video', models.CharField(blank=True, default=None, max_length=1000)),
                ('solution', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='forum.forum')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='forum.question')),
            ],
        ),
    ]
