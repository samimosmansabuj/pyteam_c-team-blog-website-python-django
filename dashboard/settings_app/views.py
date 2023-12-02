from django.shortcuts import render, redirect
from home.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
import os

# -------------------Site Settings Section Start -------------------
@login_required(login_url='login')
def site_settings(request):
    user = request.user
    if user.is_admin == False:
        return redirect('profile_settings')
    else:
        team_setting_config = Team_Setting_Config.objects.get(setting_no=1)
        context = {'team_setting_config': team_setting_config}
        
        if request.method == 'POST':
            if request.FILES.get('team_icon'):
                try:
                    if team_setting_config.team_icon != 'pyteam-c-icon.png':
                        os.remove(team_setting_config.team_icon.path)
                    team_setting_config.team_icon = request.FILES.get('team_icon')
                except:
                    team_setting_config.team_icon = request.FILES.get('team_icon')
            
            if request.FILES.get('team_logo'):
                if team_setting_config.team_logo and team_setting_config.team_logo != 'default/team-c-logo-transparent.png':
                    os.remove(team_setting_config.team_logo.path)
                team_setting_config.team_logo = request.FILES.get('team_logo')
            
            team_setting_config.team_title = request.POST['team_title']
            team_setting_config.team_designation = request.POST['team_designation']
            team_setting_config.team_address = request.POST['team_address']
            team_setting_config.team_address_upazila = request.POST['team_address_upazila']
            team_setting_config.team_address_district = request.POST['team_address_district']
            team_setting_config.team_email = request.POST['team_email']
            team_setting_config.team_phone_number = request.POST['team_phone_number']
            messages.success(request, 'Successfully Update!')
            team_setting_config.save()
            return redirect(request.META['HTTP_REFERER'])
        
        return render(request, 'dashboard/settings/site_settings/site_settings.html', context)
        
# -------------------Site Settings Section End -------------------


# -------------------Social Profile Section Start -------------------
@login_required(login_url='login')
def social_profile(request):
    user = request.user
    if user.is_admin == False:
        return redirect('profile_social_link')
    
    team_setting_config = Team_Setting_Config.objects.get(setting_no=1)
    team_social_profiles = Team_Social_Profiles.objects.get(team_setting_config=team_setting_config)
    context = {'team_social_profiles': team_social_profiles}
    if request.method == 'POST':
        if request.POST['website']:
            team_social_profiles.website = request.POST['website']
        
        if request.POST['facebook']:
            team_social_profiles.facebook = request.POST['facebook']

        if request.POST['instagram']:
            team_social_profiles.instagram = request.POST['instagram']
        
        if request.POST['twitter']:
            team_social_profiles.twitter = request.POST['twitter']
        
        if request.POST['linkedin']:
            team_social_profiles.linkedin = request.POST['linkedin']

        if request.POST['github']:
            team_social_profiles.github = request.POST['github']

        if request.POST['youtube']:
            team_social_profiles.youtube = request.POST['youtube']
        
        messages.success(request, "Update Successfully!")
        team_social_profiles.save()
        return redirect(request.META['HTTP_REFERER'])
    
    return render(request, 'dashboard/settings/site_settings/social_profile.html', context)
# -------------------Social Profile Section End -------------------


# -------------------Page Slider Settings Section Start -------------------
@login_required(login_url='login')
def about_us(request):
    user = request.user
    if user.is_admin == False:
        return redirect('profile_settings')

    team_setting_config = Team_Setting_Config.objects.get(setting_no=1)
    team_about_us = Team_About_Us.objects.get(team_setting_config=team_setting_config)
    context = {'team_about_us': team_about_us}
    
    if request.method == 'POST':
        team_profile_pic = request.FILES.get('team_profile_pic')
        if team_profile_pic:
            if team_about_us.team_profile_pic:
                os.remove(team_about_us.team_profile_pic.path)
            team_about_us.team_profile_pic = team_profile_pic
        team_about_us.team_college = request.POST['college_name']
        team_about_us.team_short_description = request.POST['short_description']
        team_about_us.team_details_description = request.POST['details_description']
        team_about_us.team_team_clients = request.POST['team_team_clients']
        team_about_us.team_projects = request.POST['team_projects']
        team_about_us.team_awards = request.POST['team_awards']
        team_about_us.save()
        messages.success(request, "Update Successfully!")
        return redirect(request.META['HTTP_REFERER'])

    
    return render(request, 'dashboard/settings/site_settings/about_us.html', context)
# -------------------Page Slider Settings Section Start -------------------


# -------------------Page Slider Settings Section Start -------------------
@login_required(login_url='login')
def page_slider_settings(request):
    user = request.user
    if user.is_admin == False:
        return redirect('profile_settings')

    team_setting_config = Team_Setting_Config.objects.get(setting_no=1)
    team_blog_slide = Team_Blog_Slide.objects.get(team_setting_config=team_setting_config)
    context = {'team_blog_slide': team_blog_slide}
    
    if request.method == 'POST':
        slide_image = request.FILES.get('slide_image')
        if slide_image:
            if team_blog_slide.slide_image and team_blog_slide.slide_image != 'slider_bg.jpg':
                os.remove(team_blog_slide.slide_image.path)
            team_blog_slide.slide_image = slide_image
        
        team_blog_slide.slide_title = request.POST['slide_title']
        team_blog_slide.title_first = request.POST['title_first']
        team_blog_slide.title_second = request.POST['title_second']
        
        messages.success(request, "Update Successfully!")
        team_blog_slide.save()
        return redirect(request.META['HTTP_REFERER'])
    
    return render(request, 'dashboard/settings/site_settings/page_slider_settings.html', context)
# -------------------Page Slider Settings Section End -------------------


@login_required(login_url='login')
def change_password_admin(request):
    user = request.user
    if user.is_admin == False:
        return redirect('change_password_member')

    if request.method == 'POST':
        user = request.user
        current_password = request.POST['current_password']
        verify_current_password = check_password(current_password, user.password)
        
        new_password = request.POST['new_password']
        re_new_password = request.POST['re_new_password']
        
        if not verify_current_password:
            messages.warning(request, "Wrong Current Passowrd!")
            return redirect(request.META['HTTP_REFERER'])
        elif new_password != re_new_password:
            messages.warning(request, "New Passowrd Does Not Match!")
            return redirect(request.META['HTTP_REFERER'])
        else:
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password Update Successfully!")
            
            email = user.email
            username = user.username
            admin_change_password_mail(email, username, new_password)
            return redirect(request.META['HTTP_REFERER'])
        
    return render(request, 'dashboard/settings/site_settings/change_password.html')

def admin_change_password_mail(email, username, new_password):
    subject = "Password Change Successfully!"
    message = f"""Dear User,
    Your account password has been change successfully!
    Your Username: {username}
    Your New Password: {new_password}"""
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)

