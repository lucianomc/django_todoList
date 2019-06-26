
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.SignUp.as_view(), name='register'),
]
