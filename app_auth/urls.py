
from django.urls import path
from .views import *


urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', login_view, name='logout'),
]