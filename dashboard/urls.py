from django.urls import path, include
from .views import *

urlpatterns = [
    path('', dashboard_home, name='dashboard_home'),
    # path('team-testimonials/', team_testimonials, name='team_testimonials'),
    path('skills/', skills_list, name='skills_list'),
    
    # path('my_profile/', my_profile, name='my_profile'),
    
    path('portfolio-category/', portfolio_category, name='portfolio_category'),
    path('delete-portfoli-category/<int:id>/', delete_portfolio_category, name='delete_portfolio_category'),
    path('edit-portfoli-category/<int:id>/', edit_portfolio_category, name='edit_portfolio_category'),
    
    path('testimonials/', testimonials, name='testimonials'),
    path('add-testimonials/', add_testimonials, name='add_testimonials'),
    path('update-testimonials/<int:id>/', update_testimonials, name='update_testimonials'),
    path('delete-testimonials/<int:id>/', delete_testimonials, name='delete_testimonials'),
    
    
    path('all-portfoli/', all_portfolio, name='all_portfolio'),
    path('add-portfoli/', add_portfolio, name='add_portfolio'),
    path('update-portfoli/<int:id>/', update_portfolio, name='update_portfolio'),
    path('delete-portfoli/<int:id>/', delete_portfolio, name='delete_portfolio'),
    
    
    
    path('team-member/', include('dashboard.team_app.urls')),
    path('settings/', include('dashboard.settings_app.urls')),
    path('profile-settings/', include('dashboard.profile_settings.urls')),
]