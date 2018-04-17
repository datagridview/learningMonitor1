"""learningMonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from dataFeedback import views
from django.contrib import admin

from dataFeedback.views import UserViewSet, ClipViewSet, api_root,HeartBeatViewSet,OperationViewSet,EmotionViewSet
from rest_framework import renderers

clip_list = ClipViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
clip_detail = ClipViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

heartbeat_list = HeartBeatViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

heartbeat_detail = HeartBeatViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

emotion_list = EmotionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

emotion_detail = EmotionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

operation_list = OperationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

operation_detail = OperationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# 
urlpatterns = format_suffix_patterns([
    url(r'^api/$', api_root),
    url(r'^admin/', admin.site.urls),
    url(r'^api/clips/$', clip_list, name='clip-list'),
    url(r'^api/clips/(?P<pk>[0-9]+)/$', clip_detail, name='clip-detail'),
    url(r'^api/users/$', user_list, name='user-list'),
    url(r'^api/users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^api/heartbeats/$', heartbeat_list, name='heartbeat-list'),
    url(r'^api/heartbeats/(?P<pk>[0-9]+)/$', heartbeat_detail, name='heartbeat-detail'),
    url(r'^api/operations/$', operation_list, name='operation-list'),
    url(r'^api/operations/(?P<pk>[0-9]+)/$', operation_detail, name='operation-detail'),
    url(r'^api/emotions/$', emotion_list, name='emotion-list'),
    url(r'^api/emotions/(?P<pk>[0-9]+)/$', emotion_detail, name='emotion-detail'),
])