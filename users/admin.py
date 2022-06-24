from django.contrib import admin
from .models import Profile,Project,ProjectPhoto,ProjectVideo,ProjectComment,ProjectCommentNotification,AnswerNotification

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(ProjectPhoto)
admin.site.register(ProjectVideo)
admin.site.register(ProjectComment)
admin.site.register(ProjectCommentNotification)
admin.site.register(AnswerNotification)