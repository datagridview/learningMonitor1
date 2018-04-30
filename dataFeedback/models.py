from django.db import models

EMOTIONS = ('anger','disgust','fear','happiness','neutral','sadness','surprise','NoFace')
EMOTIONS_OPTIONS = sorted((item,item) for item in EMOTIONS)
FLAGS = ('open','close')
FLAGS_OPTIONS = sorted((item,item) for item in FLAGS)

class Clip(models.Model):
    clip_outer_id = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    tested = models.DateTimeField()
    owner = models.ForeignKey('auth.User', related_name='clips', on_delete=models.CASCADE)


class State(models.Model):
    clip = models.ForeignKey(Clip, related_name='state',on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=False)
    heartbeats = models.IntegerField(null=True)
    emotion = models.CharField(choices=EMOTIONS_OPTIONS, max_length=20,null=True)
    process_flag = models.CharField(choices=FLAGS_OPTIONS, null=True, max_length=20)
    process_name =  models.CharField(max_length=255,null=True)
    operation_num = models.IntegerField(default=0)
    class Meta:
        ordering = ('time',)


class HeartBeat(models.Model):
    clip = models.ForeignKey(Clip, related_name='heartbeats',on_delete=models.CASCADE)
    beat_nums = models.IntegerField()
    time = models.DateTimeField(auto_now=False)
    owner = models.ForeignKey('auth.User', related_name='heartbeats_owner', on_delete=models.CASCADE)
    class Meta:
        ordering = ('time',)

class Emotion(models.Model):
    clip = models.ForeignKey(Clip, related_name='emotions',on_delete=models.CASCADE)
    state = models.CharField(choices=EMOTIONS_OPTIONS, max_length=20)
    time = models.DateTimeField(auto_now=False)
    owner = models.ForeignKey('auth.User', related_name='emotions_owner', on_delete=models.CASCADE)
    class Meta:
        ordering = ('time',)

class Operation(models.Model):
    clip = models.ForeignKey(Clip, related_name='operations',on_delete=models.CASCADE)
    keypressed_num = models.IntegerField()
    mouseclicked_num = models.IntegerField()
    alloperation_num = models.IntegerField()
    content = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='operations_owner', on_delete=models.CASCADE)

class Minutetimes(models.Model):
    operation = models.ForeignKey(Operation, related_name='minutestimes', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=False)
    times = models.IntegerField()

class Process(models.Model):
    clip = models.ForeignKey(Clip,related_name='processes', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='processes_owner', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=False)
    flag = models.CharField(choices=FLAGS_OPTIONS, max_length=20)
    process_name = models.CharField(max_length=255)