from django.shortcuts import render, redirect
from home.models import Team_Member
from personal_profile.models import About_Me, Web_Site
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def profile_settings(request):
    user = request.user
    if user.is_team_member == False:
        return redirect('site_settings')

    user = request.user
    member = Team_Member.objects.get(username=user)
    about_me = About_Me.objects.get(team_member=member)
    context = {'member': member, 'about_me': about_me}

    if request.method == 'POST':
        if request.POST['gender']:
            about_me.gender = request.POST['gender']
        if request.POST['clients']:
            print(request.POST['clients'])
            about_me.clients = request.POST['clients']
        if request.POST['projects']:
            about_me.projects = request.POST['projects']
        if request.POST['hours']:
            about_me.hours = request.POST['hours']
        if request.POST['awards']:
            about_me.awards = request.POST['awards']
        if request.POST['short_description']:
            about_me.short_description = request.POST['short_description']
        if request.POST['details_description']:
            about_me.details_description = request.POST['details_description']
        if request.POST['resume_description']:
            about_me.resume_description = request.POST['resume_description']
        if request.POST['testimonials_description']:
            about_me.testimonials_description = request.POST['testimonials_description']
        if request.POST['address']:
            about_me.address = request.POST['address']
        if request.POST['address_upazila']:
            about_me.address_upazila = request.POST['address_upazila']
        if request.POST['address_district']:
            about_me.address_district = request.POST['address_district']
        if request.POST['address_country']:
            about_me.address_country = request.POST['address_country']
        
        about_me.save()
        messages.success(request, "Team Member About Update Successfully Complete!")
        return redirect(request.META['HTTP_REFERER'])
    return render(request, 'dashboard/settings/profile_settings/profile_settings.html', context)

@login_required(login_url='login')
def profile_social_link(request):
    user = request.user
    if user.is_team_member == False:
        return redirect('social_profile')
    
    user = request.user
    member = Team_Member.objects.get(username=user)
    web_site = Web_Site.objects.get(team_member=user)
    context = {'member': member, 'web_site': web_site}
    
    if request.method == 'POST':
        if request.POST['website']:
            web_site.website = request.POST['website']
        else:
            web_site.website = None
        if request.POST['facebook']:
            web_site.facebook = request.POST['facebook']
        else:
            web_site.facebook = None
        if request.POST['instagram']:
            web_site.instagram = request.POST['instagram']
        else:
            web_site.instagram = None
        if request.POST['twitter']:
            web_site.twitter = request.POST['twitter']
        else:
            web_site.twitter = None
        if request.POST['linkedin']:
            web_site.linkedin = request.POST['linkedin']
        else:
            web_site.linkedin = None
        if request.POST['github']:
            web_site.github = request.POST['github']
        else:
            web_site.github = None
        if request.POST['youtube']:
            web_site.youtube = request.POST['youtube']
        else:
            web_site.youtube = None
        
        web_site.save()
        messages.success(request, "Social Profile Update Successfully Complete!")
        return redirect(request.META['HTTP_REFERER'])
    
    return render(request, 'dashboard/settings/profile_settings/personal_social_profile.html', context)

@login_required(login_url='login')
def change_password_member(request):
    user = request.user
    if user.is_team_member == False:
        return redirect('change_password_admin')
    
    
    if request.method == 'POST':
        user = request.user
        current_password = request.POST['current_password']
        verify_current_password = check_password(current_password, user.password)
        
        new_password = request.POST['new_password']
        re_new_password = request.POST['re_new_password']
        
        if not verify_current_password:
            messages.warning(request, "Current Password Does Not Match!")
            return redirect(request.META['HTTP_REFERER'])
        else:
            if new_password != re_new_password:
                messages.warning(request, "Password Does Not Match!")
                return redirect(request.META['HTTP_REFERER'])
            else:
                user.set_password(new_password)
                user.save()
                messages.success(request, "Password Update Successfully!")
            
                username = user.username
                email = user.email
                change_password_mail(email, username, new_password)
                return redirect(request.META['HTTP_REFERER'])

    return render(request, 'dashboard/settings/profile_settings/change_password.html')

def change_password_mail(email, username, new_password):
    subject = "Password Change Successfully!"
    message = f"""Dear User,
    Your account password has been change successfully!
    Your Username: {username}
    Your New Password: {new_password}"""
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)


