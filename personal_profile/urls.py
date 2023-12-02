from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/', personal_profile, name='personal_profile'),
    path('contact/', personal_contact, name='personal_contact'),
]