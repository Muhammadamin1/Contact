from django.urls import path
from .views import *

urlpatterns = [
    path('list/', UserListAPIView.as_view(), name='user-list'),
    path('create/', UserCreateAPIView.as_view(), name='user-create')
]
