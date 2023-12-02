from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import random
import string

# Create your views here.
def home(request):
    team_members = Team_Member.objects.all()
    team_setting = Team_Setting_Config.objects.all()
    
    
    team_setting_config = team_setting[0]
    team_blog_slide = Team_Blog_Slide.objects.get(team_setting_config=team_setting_config)
    team_about_us = Team_About_Us.objects.get(team_setting_config=team_setting_config)
    team_testimonials = Team_testimonials.objects.all()
    team_social_profiles = Team_Social_Profiles.objects.get(team_setting_config=team_setting_config)
    
    # context = {
    #     'team_members': team_members,
    # }
    context = {
        'team_members': team_members, 'team_setting_config': team_setting_config,
        'team_blog_slide': team_blog_slide, 'team_about_us': team_about_us,
        'team_testimonials': team_testimonials, 'team_social_profiles': team_social_profiles
    }
    return render(request, 'home/home.html', context)


def site_contact_mail(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        
        subject = request.POST['subject']
        message = message = request.POST['message']
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list)
        
    return redirect(request.META['HTTP_REFERER'])








def Login(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if not User.objects.filter(username=username).exists():
            messages.warning(request, "Username Does Not Match!")
            return redirect('login')
        else:
            user = authenticate(username=username, password=password)
            if not user:
                messages.warning(request, "Password Does Not Match!")
                return redirect('login')
            else:
                login(request, user)
                return redirect('dashboard_home')
    
    return render(request, 'account/login.html')



def forget_password(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home')

    if request.method == 'POST':
        email = request.POST['email']
        
        new_password = ''.join(random.choice(string.ascii_letters) for i in range(8))
        # new_password = random.randint(11111111, 99999999)
        if not Team_Member.objects.filter(email=email).exists():
            messages.warning(request, "Email Address Does Not Match!")
            return redirect('forget_password')
        else:
            team_member = Team_Member.objects.get(email=email)
            team_member.set_password(new_password)
            team_member.save()
            username = team_member.username
            
            forget_password_send(email, new_password, username)
            return redirect('login')
    
    return render(request, 'account/forget_password.html')

def forget_password_send(email, new_password, username):
    subject = "Forget Password? We Set a new password!"
    message = f"""Dear User
    Your New Password: {new_password}
    Your Username : {username}"""
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
    


# def registration(request):
#     if request.user.is_authenticated:
#         return redirect('dashboard_home')

#     return render(request, 'account/registration.html')

@login_required(login_url='login')
def Logout(request):
    logout(request)
    return redirect('login')

