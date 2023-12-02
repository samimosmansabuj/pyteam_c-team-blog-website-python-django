from django.urls import path
from .views import site_settings, social_profile, about_us, page_slider_settings, change_password_admin

urlpatterns = [
    path('', site_settings, name='site_settings'),
    path('social-profile/', social_profile, name='social_profile'),
    path('about-us/', about_us, name='about_us'),
    path('page-slider-settings/', page_slider_settings, name='page_slider_settings'),
    path('change-password/', change_password_admin, name='change_password_admin'),
]