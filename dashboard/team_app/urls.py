from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard_team_member, name='dashboard_team_member'),
    path('add-new/', add_new_member, name='add_new_member'),
    path('delete-team-member/<int:id>/', delete_team_member, name='delete_team_member'),
    path('<int:id>/', update_team_member, name='update_team_member'),
    
    path('education/', education, name='education'),
    path('add-education/', add_education, name='add_education'),
    path('update-education/<int:id>/', update_education, name='update_education'),
    path('delete-education/<int:id>/', delete_education, name='delete_education'),
    
    
    path('certificate/', all_certificate, name='certificate'),
    path('add-certificate/', add_certificate, name='add_certificate'),
    path('update-certificate/<int:id>/', update_certificate, name='update_certificate'),
    path('delete-certificate/<int:id>/', delete_certificate, name='delete_certificate'),
    
    
    path('experience/', all_experience, name='experience'),
    path('add-experience/', add_experience, name='add_experience'),
    path('update-experience/<int:id>/', update_experience, name='update_experience'),
    path('delete-experience/<int:id>/', delete_experience, name='delete_experience'),
    
    
]