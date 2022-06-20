from django.contrib import admin
from .models import Forum,Topic,Question,Answer

admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Answer)