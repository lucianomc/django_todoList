from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from .views import (TaskAPICreateView, TaskAPIListView, TaskRudView,
                    TasksUserAPIListView, TasksUserRudView,
                    TaskUserAPICreateView, UserAPIListView, UserRudView)

app_name = 'rest'

urlpatterns = [
    url(r'user/(?P<pk>\d+)/$', UserRudView.as_view(), name='user_rud'),
    url(r'user/', UserAPIListView.as_view(), name='user_list'),

    url(r'task/(?P<pk>\d+)/$', TaskRudView.as_view(), name='task_rud'),
    url(r'task/create/', TaskAPICreateView.as_view(), name='task_create'),
    url(r'task/', TaskAPIListView.as_view(), name='task_list'),

    url(r'assigneds/(?P<pk>\d+)/$', TasksUserRudView.as_view(), name='task_user_rud'),
    url(r'assigneds/create/', TaskUserAPICreateView.as_view(), name='task_user_create'),
    url(r'assigneds/', TasksUserAPIListView.as_view(), name='assigneds'),
]
