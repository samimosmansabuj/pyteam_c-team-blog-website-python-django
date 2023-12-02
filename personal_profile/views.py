from django.shortcuts import render, redirect
from home.models import *
from .models import *
from django.core.mail import send_mail

# Create your views here.
def personal_profile(request, id):
    team_member = Team_Member.objects.get(id=id)
    my_skills = team_member.skills.all()
    is_basic = int(100/4*1)
    is_medium = int(100/4*2)
    is_advanced = int(100/4*3)
    
    about_me = About_Me.objects.get(team_member=team_member)
    testimonials = Testimonials.objects.filter(team_member=team_member)
    
    portfolio_category = Portfolio_Category.objects.all()
    portfolio = Portfolio.objects.filter(team_member=team_member)
    
    experience = Experience.objects.filter(team_member=team_member)
    certification = Certification.objects.filter(team_member=team_member)
    website_link = Web_Site.objects.get(team_member=team_member)
    education = Education.objects.filter(team_member=team_member)
    
    context = {
        'team_member': team_member, 'website_link': website_link,
        'about_me': about_me, 'testimonials': testimonials, 'portfolio': portfolio, 'experience': experience,
        'certification': certification, 'education': education, 'portfolio_category': portfolio_category, 'my_skills': my_skills,
        'is_basic': is_basic, 'is_medium': is_medium, 'is_advanced': is_advanced
    }
    
    if education:
        last_education = education[0]
        context['last_education'] = last_education
    
    return render(request, 'personal_profile/personal_profile.html', context)

def personal_contact(request):
    if request.method == 'POST':
        mailer_name = request.POST['mailer_name']
        to_mail = request.POST['to_mail']
        mail_subject = request.POST['mail_subject']
        mail_message = request.POST['mail_message']
        team_member_id = request.POST['id']
        team_member = Team_Member.objects.get(id=team_member_id)
        
        subject = mail_subject
        message = mail_message
        from_email = team_member.email
        recipient_list = [to_mail]
        send_mail(subject, message, from_email, recipient_list)
        
    return redirect(request.META['HTTP_REFERER'])


