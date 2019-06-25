from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from .views import TaskUserViewSet, TaskViewSet, UserViewSet

app_name = 'rest'

router = routers.DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'tasksusers', TaskUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
