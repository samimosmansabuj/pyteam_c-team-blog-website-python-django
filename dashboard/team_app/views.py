from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import *
from personal_profile.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
import os

# Create your views here.
@login_required(login_url='login')
def dashboard_team_member(request):
    team_member = Team_Member.objects.all()
    context = {'team_member': team_member}
    return render(request, 'dashboard/dashboard_home/team_member/team_member.html', context)


# -------------Team Add Saction Start----------------
@login_required(login_url='login')
def update_team_member(request, id):
    if request.user.is_admin == False:
        return redirect('dashboard_home')
    
    team_member = Team_Member.objects.get(id=id)
    if request.method == 'POST':
        team_member.name = request.POST['name']
        team_member.phone_number = request.POST['phone_number']
        team_member.email = request.POST['email']
        team_member.designation = request.POST['designation']
        team_member.date_of_birth = request.POST['date_of_birth']
        team_member.gender = request.POST['gender']
        team_member.username = request.POST['username']
        
        if request.FILES.get('image'):
            if team_member.image:
                if team_member.image != 'default/default_team_member_image.png':
                    os.remove(team_member.image.path)
            team_member.image = request.FILES.get('image')
        
        if request.FILES.get('cover_image'):
            if team_member.cover_image:
                if team_member.cover_image != 'default/default_team_member_cover_image.jpg':
                    os.remove(team_member.cover_image.path)
            team_member.cover_image = request.FILES.get('cover_image')
        
        if request.POST['short_description']:
            team_member.short_description = request.POST['short_description']
        status = request.POST['status']
        if status == 'Active':
            team_member.is_varified = True
        elif status == 'Inactive':
            team_member.is_varified = False
        
        team_member.save()
        messages.success(request, "Team Member Update Successfully Complete!")
        return redirect('dashboard_team_member')
    
    return render(request, 'dashboard/dashboard_home/team_member/update_team_member.html', {'team_member': team_member})

@login_required(login_url='login')
def delete_team_member(request, id):
    if request.user.is_admin == False:
        return redirect('dashboard_home')
    
    team_member = Team_Member.objects.get(id=id)
    if team_member.image != 'default/default_team_member_image.png':
        os.remove(team_member.image.path)
    if team_member.cover_image != 'default/default_team_member_cover_image.jpg':
        os.remove(team_member.cover_image.path)
    team_member.delete()
    messages.success(request, "Team Member Delete Successfully Complete!")
    return redirect('dashboard_team_member')



#Add Section - Team member Start
@login_required(login_url='login')
def add_new_member(request):
    if request.user.is_admin == False:
        return redirect('dashboard_home')
    
    skills = Skills.objects.all()
    context = {'skills': skills}
    if request.method == 'POST':
        password =request.POST['password']
        status =request.POST['status']
        member = Team_Member.objects.create(
            name = request.POST['name'],
            phone_number = request.POST['phone_number'],
            email = request.POST['email'],
            username =request.POST['username'],
            designation = request.POST['designation'],
            gender = request.POST['gender'],
            date_of_birth = request.POST['date_of_birth'],
        )
        member.set_password(password)
        member.is_team_member = True
        
        if request.FILES.get('image'):
            member.image = request.FILES.get('image')
        if request.FILES.get('cover_image'):
            member.cover_image = request.FILES.get('cover_image')
        if request.POST['short_description']:
            member.short_description = request.POST['short_description']
        
        if status == 'Active':
            member.is_varified = True
        elif status == 'Inactive':
            member.is_varified = False
        member.save()

        team_about_me_create(member)
        team_social_link_create(member)
        Team_Create_Mail(member.email, password, member.username)
        messages.success(request, "Team Member Add Successfully Complete!")
        return redirect('dashboard_team_member')
    return render(request, 'dashboard/dashboard_home/team_member/add_team_member.html', context)

def team_social_link_create(member):
    social_link = Web_Site.objects.create(
        team_member = member,
        website = 'yourwebsite.html'
    )
    social_link.save()

def team_about_me_create(member):
    about_me = About_Me.objects.create(
        team_member = member,
        gender = member.gender,
    )
    about_me.save()

def Team_Create_Mail(email, password, username):
    subject = "Congratulations For Add Our Member!"
    message = f"""Dear User,
    Welcome to Pyteam-C
    Congratulations for add our Member!
    Your Mail: {email}
    Your Username: {username}
    Your Password:{password}
    
    Website: https://www.pyteam-c.com/
    Admin Panel: http://127.0.0.1:8000/dashboard/"""
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
#Add Section - Team member End

# -------------Team Add Saction End----------------



# -------------Educations Saction Start----------------
@login_required(login_url='login')
def education(request):
    user = request.user
    if user.is_admin == True:
        edu = Education.objects.all()
    elif user.is_team_member == True:
        edu = Education.objects.filter(team_member=user)
        
    item_per_page = 5
    
    page = request.GET.get('page')
    paginator = Paginator(edu, item_per_page)
    
    try:
        educations = paginator.page(page)
    except EmptyPage:
        educations = paginator.page(1)
    except PageNotAnInteger:
        educations = paginator.page(1)
    except InvalidPage:
        educations = paginator.page(1)

    context = {'educations': educations, 'paginator': paginator}

    return render(request, 'dashboard/education/education.html', context)


@login_required(login_url='login')
def add_education(request):
    member = []
    user = request.user
    if user.is_admin == True:
        member = Team_Member.objects.all()
    elif user.is_team_member == True:
        member = Team_Member.objects.get(username=user)
    context = {'member': member }
    
    if request.method == 'POST':
        member_id = request.POST['member']
        member = Team_Member.objects.get(id=member_id)
        status = request.POST['status']
        
        education = Education.objects.create(
            team_member = member,
            degree_name = request.POST['degree_name'],
            subject = request.POST['subject'],
            institute_name = request.POST['institute_name'],
            starting_date = request.POST['starting_date'],
            duration = request.POST['duration'],
        )
        
        if request.POST['institute_address']:
            education.institute_address = request.POST['institute_address']
        if request.POST['short_description']:
            education.short_description = request.POST['short_description']
        if request.POST['result']:
            education.result = request.POST['result']
        
        if status == 'Yes':
            education.is_complete = True
        elif status == 'No':
            education.is_complete = False
        
        if request.POST['ending_date']:
            education.ending_date = request.POST['ending_date']
            education.is_complete = True
        
        education.save()
        messages.success(request, 'Create Education Qualification Successfully!')
        return redirect('education')

    return render(request, 'dashboard/education/add_aducation.html', context)

@login_required(login_url='login')
def update_education(request, id):
    education = Education.objects.get(id=id)
    member = []
    user = request.user
    if user.is_admin == True:
        member = Team_Member.objects.all()
    elif user.is_team_member == True:
        member = Team_Member.objects.get(username=user)
        
        if member != education.team_member:
            return redirect('education')
    
    context = {'member': member, 'education': education}
    
    if request.method == 'POST':
        member_id = request.POST['member']
        member = Team_Member.objects.get(id=member_id)
        status = request.POST['status']
        
        education.team_member = member
        education.degree_name = request.POST['degree_name']
        education.subject = request.POST['subject']
        education.institute_name = request.POST['institute_name']
        education.starting_date = request.POST['starting_date']
        education.duration = request.POST['duration']
        if request.POST['institute_address']:
            education.institute_address = request.POST['institute_address']
        if request.POST['short_description']:
            education.short_description = request.POST['short_description']
        if request.POST['result']:
            education.result = request.POST['result']
        
        if status == 'Yes':
            education.is_complete = True
        elif status == 'No':
            education.is_complete = False
        
        if request.POST['ending_date']:
            education.ending_date = request.POST['ending_date']
            education.is_complete = True
        
        education.save()
        messages.success(request, 'Update Education Qualification Successfully!')
        return redirect('education')
    
    return render(request, 'dashboard/education/update_education.html', context)

@login_required(login_url='login')
def delete_education(request, id):
    education = Education.objects.get(id=id)
    user = request.user
    if user.is_team_member == True:
        member = Team_Member.objects.get(username=user)
        if member != education.team_member:
            return redirect('education')
    
    education = Education.objects.get(id=id)
    education.delete()
    messages.success(request, 'Delete Education Qualification Successfully!')
    return redirect('education')
# -------------Educations Saction Start----------------


# -------------Certificate Saction Start----------------
@login_required(login_url='login')
def all_certificate(request):
    user = request.user
    if user.is_admin == True:
        cert = Certification.objects.all()
    elif user.is_team_member == True:
        cert = Certification.objects.filter(team_member=user)
    
    item_per_page = 5
    page = request.GET.get('page')
    paginator = Paginator(cert, item_per_page)
    
    try:
        certificate = paginator.page(page)
    except EmptyPage:
        certificate = paginator.page(1)
    except PageNotAnInteger:
        certificate = paginator.page(1)
    except InvalidPage:
        certificate = paginator.page(1)
    
    context = {'certificate': certificate, 'paginator': paginator}
    return render(request, 'dashboard/certificate/certificate.html', context)

@login_required(login_url='login')
def add_certificate(request):
    member = []
    user = request.user
    if user.is_admin == True:
        member = Team_Member.objects.all()
    elif user.is_team_member == True:
        member = Team_Member.objects.get(username=user)

    context = {'member': member }
    
    if request.method == 'POST':
        member_id = request.POST['member']
        member = Team_Member.objects.get(id=member_id)
        status = request.POST['status']
        
        certificate = Certification.objects.create(
            team_member = member,
            course_name = request.POST['course_name'],
            year = request.POST['year'],
            institute_name = request.POST['institute_name'],
            starting_date = request.POST['starting_date'],
            duration = request.POST['duration'],
        )
        if request.POST['institute_address']:
            certificate.institute_address = request.POST['institute_address']
        if request.POST['short_description']:
            certificate.short_description = request.POST['short_description']

        if status == 'Yes':
            certificate.is_complete = True
        elif status == 'No':
            certificate.is_complete = False
        if request.POST['ending_date']:
            certificate.ending_date = request.POST['ending_date']
            certificate.is_complete = True
        
        certificate.save()
        messages.success(request, 'Add Certificate Successfully!')
        return redirect('certificate')
    return render(request, 'dashboard/certificate/add_certificate.html', context)

@login_required(login_url='login')
def update_certificate(request, id):
    certificate = Certification.objects.get(id=id)
    member = []
    user = request.user
    if user.is_admin == True:
        member = Team_Member.objects.all()
    elif user.is_team_member == True:
        member = Team_Member.objects.get(username=user)
        if member != certificate.team_member:
            return redirect('certificate')
    
    context = {'member': member, 'certificate': certificate}
    
    if request.method == 'POST':
        member_id = request.POST['member']
        member = Team_Member.objects.get(id=member_id)
        status = request.POST['status']
        
        certificate.team_member = member
        certificate.course_name = request.POST['course_name']
        certificate.year = request.POST['year']
        certificate.institute_name = request.POST['institute_name']
        certificate.starting_date = request.POST['starting_date']
        certificate.duration = request.POST['duration']
        if request.POST['institute_address']:
            certificate.institute_address = request.POST['institute_address']
        else:
            certificate.institute_address = None
        if request.POST['short_description']:
            certificate.short_description = request.POST['short_description']
        else:
            certificate.short_description = None
        
        if status == 'Yes':
            certificate.is_complete = True
        elif status == 'No':
            certificate.is_complete = False
        if request.POST['ending_date']:
            certificate.ending_date = request.POST['ending_date']
        else:
            certificate.ending_date = None
            
        if certificate.ending_date:
            certificate.is_complete = True
        else:
            certificate.is_complete = False
        
        certificate.save()
        messages.success(request, 'Update Certificate Successfully!')
        return redirect('certificate')
    
    return render(request, 'dashboard/certificate/update_certificate.html', context)

@login_required(login_url='login')
def delete_certificate(request, id):
    certificate = Certification.objects.get(id=id)
    user = request.user
    if user.is_team_member == True:
        member = Team_Member.objects.get(username=user)
        if member != certificate.team_member:
            return redirect('certificate')
    
    certificate.delete()
    messages.success(request, 'Delete Certificate Successfully!')
    return redirect('certificate')
# -------------Certificate Saction Start----------------



# -------------experience Saction Start----------------
@login_required(login_url='login')
def all_experience(request):
    user = request.user
    if user.is_admin == True:
        exper = Experience.objects.all()
    elif user.is_team_member == True:
        exper = Experience.objects.filter(team_member=user)
    
    item_per_page = 5
    page = request.GET.get('page')
    paginator = Paginator(exper, item_per_page)
    
    try:
        experience = paginator.page(page)
    except EmptyPage:
        experience = paginator.page(1)
    except PageNotAnInteger:
        experience = paginator.page(1)
    except InvalidPage:
        experience = paginator.page(1)
    
    context = {'experience': experience, 'paginator': paginator}
    
    return render(request, 'dashboard/experience/experience.html', context)

@login_required(login_url='login')
def add_experience(request):
    member = []
    user = request.user
    if user.is_admin == True:
        member = Team_Member.objects.all()
    elif user.is_team_member == True:
        member = Team_Member.objects.get(username=user)
    
    context = {'member': member }
    
    if request.method == 'POST':
        member_id = request.POST['member']
        member = Team_Member.objects.get(id=member_id)
        
        experience = Experience.objects.create(
            team_member = member,
            post_name = request.POST['post_name'],
            company_name = request.POST['company_name'],
            starting_date = request.POST['starting_date'],
        )
        if request.POST['ending_date']:
            experience.ending_date = request.POST['ending_date']
            experience.is_complete = True
        else:
            experience.is_complete = False
            
        if request.POST['address']:
            experience.address = request.POST['address']
        if request.POST['short_description']:
            experience.short_description = request.POST['short_description']
        
        experience.save()
        messages.success(request, 'Add Experience Successfully!')
        return redirect('experience')
    return render(request, 'dashboard/experience/add_experience.html', context)

@login_required(login_url='login')
def update_experience(request, id):
    experience = Experience.objects.get(id=id)
    member = []
    user = request.user
    if user.is_admin == True:
        member = Team_Member.objects.all()
    elif user.is_team_member == True:
        member = Team_Member.objects.get(username=user)
        if member != experience.team_member:
            return redirect('experience')
    
    context = {'member': member, 'experience': experience}
    
    if request.method == 'POST':
        member_id = request.POST['member']
        member = Team_Member.objects.get(id=member_id)
        
        experience.team_member = member
        experience.post_name = request.POST['post_name']
        experience.company_name = request.POST['company_name']
        experience.starting_date = request.POST['starting_date']
        
        if request.POST['ending_date']:
            experience.ending_date = request.POST['ending_date']
            experience.is_active = True
        else:
            experience.ending_date = None
            experience.is_active = False
            
        if request.POST['address']:
            experience.address = request.POST['address']
        else:
            experience.institute_address = None
        if request.POST['short_description']:
            experience.short_description = request.POST['short_description']
        else:
            experience.short_description = None
        
        experience.save()
        messages.success(request, 'Update Experience Successfully!')
        return redirect('experience')
    
    return render(request, 'dashboard/experience/update_experience.html', context)

@login_required(login_url='login')
def delete_experience(request, id):
    experience = Experience.objects.get(id=id)
    member = []
    user = request.user
    if user.is_team_member == True:
        member = Team_Member.objects.get(username=user)
        if member != experience.team_member:
            return redirect('experience')
        
    experience.delete()
    messages.success(request, 'Delete Experience Successfully!')
    return redirect('experience')
# -------------experience Saction Start----------------



