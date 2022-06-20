from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Classroom
from forum.models import Forum

@receiver(post_save,sender=Classroom)
def create_forum(sender,instance,created,**kwargs):
    if created:
        Forum.objects.create(classroom=instance)