from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    # path('registration/', registration, name='registration'),
    path('forget-password/', forget_password, name='forget_password'),
    path('contact-mail/', site_contact_mail, name='site_contact_mail'),
]