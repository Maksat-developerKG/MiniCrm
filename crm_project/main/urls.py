from django.urls import path
from .views import index, user_profile

urlpatterns = [
    path('', index, name='index'),
    path('users/<str:username>/', user_profile, name='user_profile'),
]