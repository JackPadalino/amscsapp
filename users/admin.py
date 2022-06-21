from django.contrib import admin
from .models import Profile,Project,ProjectPhoto,Comment,CommentNotification,AnswerNotification

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(ProjectPhoto)
admin.site.register(Comment)
admin.site.register(CommentNotification)
admin.site.register(AnswerNotification)