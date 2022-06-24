from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import ProjectComment,ProjectCommentNotification,AnswerNotification
from users.models import Profile
from forum.models import Answer

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()

@receiver(post_save,sender=ProjectComment)
def create_comment_notification(sender,instance,created,**kwargs):
    if created:
        ProjectCommentNotification.objects.create(comment=instance,notified_user=instance.project.user)


@receiver(post_save,sender=Answer)
def create_answer_notification(sender,instance,created,**kwargs):
    if created:
        AnswerNotification.objects.create(answer=instance,notified_user=instance.question.author)