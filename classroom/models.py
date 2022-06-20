from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# school year model
class SchoolYear(models.Model):
    year = models.IntegerField(default=1900)

    def get_absolute_url(self):
        return reverse('school_year-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f'{self.year}'

# classroom model
class Classroom(models.Model):
    title = models.CharField(max_length=50,default='My Classroom')
    school_year = models.ForeignKey(SchoolYear,on_delete=models.CASCADE,related_name='classrooms')
    join_code = models.CharField(max_length=10,default='abc123')
    
    def get_absolute_url(self):
        return reverse('classroom-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f'{self.title} - {self.school_year}'