from django.contrib import admin

from .models import Emotion, Clip, HeartBeat, Operation, Minutetimes, State
from django.contrib.auth.models import User

class ClipAdmin(admin.ModelAdmin):
    list_display = ('id','clip_outer_id','owner',) #添加字段显示
    search_fields = ['id','clip_outer_id','owner__username'] #添加快速查询栏

class EmotionAdmin(admin.ModelAdmin):
    list_display = ('id','owner','state') #添加字段显示
    search_fields = ['id','owner__username','state'] #添加快速查询栏

class HeartBeatAdmin(admin.ModelAdmin):
    list_display = ('id','owner','beat_nums') #添加字段显示
    search_fields = ['id','owner__username','beat_nums'] #添加快速查询栏

class OperationAdmin(admin.ModelAdmin):
    list_display = ('id','owner','keypressed_num','mouseclicked_num','alloperation_num') #添加字段显示
    search_fields = ['id','owner__username'] #添加快速查询栏

class MinutetimesAdmin(admin.ModelAdmin):
    list_display = ('id','operation','times') #添加字段显示
    search_fields = ['id','operation'] #添加快速查询栏

# admin.site.register(User)
admin.site.register(Emotion,EmotionAdmin)
admin.site.register(Clip,ClipAdmin)
admin.site.register(HeartBeat,HeartBeatAdmin)
admin.site.register(Operation,OperationAdmin)
admin.site.register(Minutetimes,MinutetimesAdmin)
admin.site.register(State)