from rest_framework import serializers
from dataFeedback.models import Clip,HeartBeat,Emotion,Operation
from django.contrib.auth.models import User

class HeartBeatSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    clip_outer_id = serializers.ReadOnlyField(source='clip.clip_outer_id')
    
    class Meta:
        model = HeartBeat
        fields = ('url','owner','clip','clip_outer_id','beat_nums','time')

class MiniHeartBeatSerializer(serializers.ModelSerializer):  
    class Meta:
        model = HeartBeat
        fields = ('time','beat_nums')

class EmotionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    clip_outer_id = serializers.ReadOnlyField(source='clip.clip_outer_id')
    # clip_outer_id = serializers.ModelField(model_field=Clip._meta.get_field('clip_outer_id'))
    class Meta:
        model = Emotion
        fields = ('url','owner','clip','clip_outer_id','state','time')

class MiniEmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ('time','state')

class OperationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    clip_outer_id = serializers.ReadOnlyField(source='clip.clip_outer_id')
    class Meta:
        model = Operation
        fields = ('url','owner','clip','clip_outer_id','keypressed_num','mouseclicked_num','alloperation_num','content')


class ClipSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # heartbeats = HeartBeatSerializer(many=True, read_only=True)
    # heartbeats = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='beat_nums'
    #  )
    heartbeats = MiniHeartBeatSerializer(many=True, read_only=True)
    emotions = MiniEmotionSerializer(many=True, read_only=True)
    operations = OperationSerializer(many=True, read_only=True)
    class Meta:
        model = Clip
        fields = ('id','url','clip_outer_id','tested', 'owner', 'heartbeats','emotions','operations')   

class UserSerializer(serializers.ModelSerializer):
    clips = serializers.HyperlinkedRelatedField(many=True,view_name='clip-detail', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'clips')


# import dateutil.parser
# dateutil.parser.parse('2008-04-10 11:47:58-05')