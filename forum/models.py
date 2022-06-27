from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from classroom.models import Classroom

# forum model
class Forum(models.Model):
    classroom = models.OneToOneField(Classroom,on_delete=models.CASCADE)

    #def get_absolute_url(self):
    #    return reverse('forum-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f'{self.classroom}'

# topic model
class Topic(models.Model):
    title = models.CharField(max_length=100,default=None)
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE,related_name='topics')

    #def get_absolute_url(self):
    #    return reverse('topic-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f'{self.title}'

# question model
class Question(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='questions')
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE,related_name='questions')
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='questions')
    title = models.CharField(max_length=100,default=None)
    content = models.CharField(max_length=500)
    project_link = models.CharField(max_length=1000,blank=True,default=None)
    image = models.ImageField(blank=True,default=None)
    video = models.CharField(max_length=1000,blank=True,default=None)
    date_posted = models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self):
        return reverse('question-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        return f"{self.title} - {self.author.first_name} {self.author.last_name} - {self.date_posted}"

# answer model
class Answer(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='answers')
    forum = models.ForeignKey(Forum,on_delete=models.CASCADE,related_name='answers')
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answers')
    content = models.CharField(max_length=500)
    project_link = models.CharField(max_length=1000,blank=True,default=None)
    image = models.ImageField(blank=True,default=None)
    video = models.CharField(max_length=1000,blank=True,default=None)
    solution = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('answer-details',kwargs={'pk':self.category.pk})

    def __str__(self):
        if self.solution == True:
            return f" {self.question.title} - {self.author.first_name} {self.author.last_name} - {self.date_posted} - MARKED AS SOLUTION"
        else:
            return f"{self.question.title} - {self.author.first_name} {self.author.last_name} - {self.date_posted}"