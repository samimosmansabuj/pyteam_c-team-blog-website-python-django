from django.contrib import admin
from .models import *

# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'joined_date']


class AdminTeam_Member(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'joined_date']
    


admin.site.register(User, AdminUser)
admin.site.register(Team_Member, AdminTeam_Member)
admin.site.register(Skills)

admin.site.register(Team_Setting_Config)
admin.site.register(Team_Blog_Slide)
admin.site.register(Team_About_Us)
admin.site.register(Team_testimonials)
admin.site.register(Team_Social_Profiles)