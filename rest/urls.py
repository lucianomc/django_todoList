from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from .views import (TaskAPIListView, TaskAPIView, TaskRudSet, UserAPIListView,
                    UserRudSet)

app_name = 'rest'

urlpatterns = [
    url(r'user/(?P<pk>\d+)/$', UserRudSet.as_view(), name='user_rud'),
    url(r'user/list/', UserAPIListView.as_view(), name='user_list'),
    
    url(r'task/create/', TaskAPIView.as_view(), name='task_create'),
    url(r'task/list/', TaskAPIListView.as_view(), name='task_list'),
    url(r'task/(?P<pk>\d+)/$', TaskRudSet.as_view(), name='task_rud'),
]
