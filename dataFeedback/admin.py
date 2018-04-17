from django.contrib import admin

from .models import Emotion, Clip, HeartBeat, Operation
from django.contrib.auth.models import User

# admin.site.register(User)
admin.site.register(Emotion)
admin.site.register(Clip)
admin.site.register(HeartBeat)
admin.site.register(Operation)