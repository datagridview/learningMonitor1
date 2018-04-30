from dataFeedback.models import Clip,HeartBeat,Emotion,Operation,Minutetimes,Process,State
from dataFeedback.serializers import HeartBeatSerializer,EmotionSerializer,UserSerializer,OperationSerializer,ClipSerializer,MinutestimesSerializer,ProcessSerializer,StateSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from dataFeedback.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from dataFeedback.pagination import StandardResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'clips': reverse('clip-list', request=request, format=format),
        'emotions': reverse('emotion-list', request=request, format=format),
        'operations': reverse('operation-list', request=request, format=format),
        'heartbeats': reverse('heartbeat-list', request=request, format=format),
        'minutestimes': reverse('minutestimes-list', request=request, format=format),
        'processes': reverse('process-list', request=request, format=format),
        'states':reverse('state-list', request=request, format=format),
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MinutestimesViewSet(viewsets.ModelViewSet):
    queryset = Minutetimes.objects.all()
    serializer_class = MinutestimesSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,)
    ordering_fields = ('time','times')
    filter_fields = ('operation',)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(operation_id=self.request.POST.get('operation', False))

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('owner','clip','clip__clip_outer_id')
    search_fields = ['owner__username','clip__clip_outer_id']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(clip_id=self.request.POST.get('clip', False),owner=self.request.user)

class ClipViewSet(viewsets.ModelViewSet):
    queryset = Clip.objects.all()
    serializer_class = ClipSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('tested',)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class HeartBeatViewSet(viewsets.ModelViewSet):
    queryset = HeartBeat.objects.all()
    serializer_class = HeartBeatSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('owner','clip','clip__clip_outer_id')
    search_fields = ['owner__username','clip__clip_outer_id']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EmotionViewSet(viewsets.ModelViewSet):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter,)
    ordering_fields = ('time',)
    filter_fields = ('owner','clip__clip_outer_id','state')
    search_fields = ['owner__username','clip__clip_outer_id']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(clip_id=self.request.POST.get('clip', False),owner=self.request.user)

class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter,)
    ordering_fields = ('time',)
    filter_fields = ('owner','clip__clip_outer_id','flag')
    search_fields = ['owner__username','clip__clip_outer_id']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(clip_id=self.request.POST.get('clip', False),owner=self.request.user)

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter,)
    ordering_fields = ('time',)
    filter_fields = ('clip__clip_outer_id','emotion','process_flag','operation_num')
    search_fields = ['clip__clip_outer_id',]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(clip_id=self.request.POST.get('clip', False))