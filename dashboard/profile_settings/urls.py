from django.urls import path
from .views import profile_settings, profile_social_link, change_password_member

urlpatterns = [
    path('', profile_settings, name='profile_settings'),
    path('social_link/', profile_social_link, name='profile_social_link'),
    path('change-password/', change_password_member, name='change_password_member'),
]