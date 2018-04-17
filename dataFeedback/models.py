from django.db import models

EMOTIONS = ('anger','disgust','fear','happiness','neutral','sadness','surprise','NoFace')
EMOTIONS_OPTIONS = sorted((item,item) for item in EMOTIONS)

class Clip(models.Model):
    clip_outer_id = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    tested = models.DateTimeField()
    owner = models.ForeignKey('auth.User', related_name='clips', on_delete=models.CASCADE)


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