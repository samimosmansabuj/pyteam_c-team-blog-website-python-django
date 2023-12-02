from django.shortcuts import render, redirect
from personal_profile.models import Testimonials
from home.models import *
from personal_profile.models import *
from django.contrib import messages
import os
from django.contrib.auth.decorators import login_required
from home.models import Team_Setting_Config
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage

# Create your views here.
@login_required(login_url='login')
def dashboard_home(request):
    team_member = Team_Member.objects.all()
    project = Portfolio.objects.all()
    testimonial = Testimonials.objects.all()
    context = {'team_member': team_member, 'project': project, 'testimonial': testimonial}
    return render(request, 'dashboard/dashboard_home/dashboard_home.html', context)

@login_required(login_url='login')
def skills_list(request):
    skill = Skills.objects.all()
    
    item_per_page = 8
    paginator = Paginator(skill, item_per_page)
    page = request.GET.get('page')
    try:
        skills = paginator.page(page)
    except EmptyPage:
        skills = paginator.page(1)
    except PageNotAnInteger:
        skills = paginator.page(1)
    except InvalidPage:
        skills = paginator.page(1)
    
    context = {'skills': skills, 'paginator': paginator}
    return render(request, 'dashboard/dashboard_home/skills_list.html', context)

# def team_testimonials(request):
#     # testimonials = Team_testimonials.objects.all()
#     testimonials = Testimonials.objects.all()
#     context = {'testimonials': testimonials}
#     return render(request, 'dashboard/dashboard_home/team_testimonials.html', context)


# -------------Portfolio Category Saction Start----------------
@login_required(login_url='login')
def portfolio_category(request):
    if request.user.is_admin == False:
        return redirect('dashboard_home')
    
    portfoli_categories = Portfolio_Category.objects.all()
    
    item_per_page = 8
    paginator = Paginator(portfoli_categories, item_per_page)
    page = request.GET.get('page')
    try:
        portfoli_category = paginator.page(page)
    except EmptyPage:
        portfoli_category = paginator.page(1)
    except PageNotAnInteger:
        portfoli_category = paginator.page(1)
    except InvalidPage:
        portfoli_category = paginator.page(1)
    
    context = {'content': portfoli_category, 'paginator': paginator}
    
    if request.method == 'POST':
        portfolio_category_name = request.POST['portfolio_category_name']
        portfoli_category = Portfolio_Category.objects.create(title=portfolio_category_name)
        portfoli_category.save()
        messages.success(request, 'Add New Successfully!')
        return redirect(request.META['HTTP_REFERER'])
    
    return render(request, 'dashboard/dashboard_home/portfolio/portfoli_category.html', context)

@login_required(login_url='login')
def delete_portfolio_category(request, id):
    if request.user.is_admin == False:
        return redirect('dashboard_home')
    
    portfolio_category = Portfolio_Category.objects.get(id=id)
    portfolio_category.delete()
    messages.success(request, 'Portfolio Category Delete Successfully!')
    return redirect(request.META['HTTP_REFERER'])

@login_required(login_url='login')
def edit_portfolio_category(request, id):
    if request.user.is_admin == False:
        return redirect('dashboard_home')
    
    portfolio_category = Portfolio_Category.objects.get(id=id)
    if request.method == 'POST':
        portfolio_category.title = request.POST['portfolio_category_name']
        portfolio_category.save()
        messages.success(request, 'Portfolio Category Udpate Successfully!')
        return redirect('portfolio_category')
    
    return render(request, 'dashboard/dashboard_home/portfolio/edit_portfolio_category.html', {'portfolio_category': portfolio_category})
# -------------Portfolio Category Saction Start----------------




# -------------Portfolio Saction Start----------------
#---------------This Section Only For Admin or Staff------------------------------
@login_required(login_url='login')
def all_portfolio(request):
    user = request.user
    if user.is_admin == True:
        all_portfolio = Portfolio.objects.all()
    elif user.is_team_member == True:
        all_portfolio = Portfolio.objects.filter(team_member=user)
    
    
    item_per_page = 8
    paginator = Paginator(all_portfolio, item_per_page)
    page = request.GET.get('page')
    try:
        portfolio = paginator.page(page)
    except EmptyPage:
        portfolio = paginator.page(1)
    except PageNotAnInteger:
        portfolio = paginator.page(1)
    except InvalidPage:
        portfolio = paginator.page(1)
    
    context = {'content': portfolio, 'paginator': paginator}
    return render(request, 'dashboard/dashboard_home/portfolio/all_portfolio.html', context)

@login_required(login_url='login')
def add_portfolio(request):
    user = request.user
    if user.is_admin == True:
        member = Team_Member.objects.all()
    elif user.is_team_member == True:
        member = Team_Member.objects.get(username=user)
    
    portfolio_category = Portfolio_Category.objects.all()
    context = {'member': member, 'portfolio_category': portfolio_category}
    
    if request.method == 'POST':
        member_id = request.POST['member']
        member = Team_Member.objects.get(id=member_id)
        category_id = request.POST['category']
        category = Portfolio_Category.objects.get(id=category_id)
        status = request.POST['status']
        
        portfolio = Portfolio.objects.create(
            team_member = member,
            portfolio_category = category,
            title = request.POST['title'],
            details = request.POST['details'],
            short_description = request.POST['short_description'],
            link = request.POST['link'],
        )
        if status == 'Active':
            portfolio.is_active = True
        elif status == 'Inactive':
            portfolio.is_active = False
        
        if request.FILES.get('portfolio_image'):
            portfolio.portfolio_image = request.FILES.get('portfolio_image')
        
        if request.FILES.get('portfolio_cover_image'):
            portfolio.portfolio_cover_image = request.FILES.get('portfolio_cover_image')
        
        portfolio.save()
        messages.success(request, 'Portfolio Create Successfully!')
        return redirect('all_portfolio')
    
    return render(request, 'dashboard/dashboard_home/portfolio/add_portfolio.html', context)

@login_required(login_url='login')
def update_portfolio(request, id):
    user = request.user
    if user.is_admin == True:
        member = Team_Member.objects.all()
    elif user.is_team_member == True:
        member = Team_Member.objects.get(username=user)

    portfolio_category = Portfolio_Category.objects.all()
    portfolio = Portfolio.objects.get(id=id)
    context = {'member': member, 'portfolio_category': portfolio_category, 'portfolio': portfolio}
    
    if request.method == 'POST':
        member_id = request.POST['member']
        member = Team_Member.objects.get(id=member_id)
        category_id = request.POST['category']
        category = Portfolio_Category.objects.get(id=category_id)
        
        portfolio.team_member = member
        portfolio.portfolio_category = category
        portfolio.title = request.POST['title']
        portfolio.details = request.POST['details']
        portfolio.short_description = request.POST['short_description']
        portfolio.link = request.POST['link']
        
        status = request.POST['status']
        if status == 'Active':
            portfolio.is_active = True
        elif status == 'Inactive':
            portfolio.is_active = False
        
        if request.FILES.get('portfolio_image'):
            if portfolio.portfolio_image != 'default/default_portfoli_image.jpg':
                os.remove(portfolio.portfolio_image.path)
            portfolio.portfolio_image = request.FILES.get('portfolio_image')
        
        if request.FILES.get('portfolio_cover_image'):
            if portfolio.portfolio_cover_image:
                os.remove(portfolio.portfolio_cover_image.path)
            portfolio.portfolio_cover_image = request.FILES.get('portfolio_cover_image')
        
        portfolio.save()
        messages.success(request, 'Portfolio Update Successfully!')
        return redirect('all_portfolio')
    
    return render(request, 'dashboard/dashboard_home/portfolio/update_portfolio.html', context)

@login_required(login_url='login')
def delete_portfolio(request, id):
    portfolio = Portfolio.objects.get(id=id)
    if portfolio.portfolio_image and portfolio.portfolio_image != 'default/default_portfoli_image.jpg':
        os.remove(portfolio.portfolio_image.path)
    if portfolio.portfolio_cover_image:
        os.remove(portfolio.portfolio_cover_image.path)
    portfolio.delete()
    messages.success(request, 'Portfolio Delete Successfully!')
    return redirect(request.META['HTTP_REFERER'])
# -------------Portfolio Saction End----------------



# -------------Testimonials Saction Start----------------
@login_required(login_url='login')
def testimonials(request):
    user = request.user
    if user.is_admin == True:
        testimonial_all = Testimonials.objects.all()
    elif user.is_team_member == True:
        testimonial_all = Testimonials.objects.filter(team_member=user)
    
    item_per_page = 5
    
    page = request.GET.get('page')
    paginator = Paginator(testimonial_all, item_per_page)
    
    try:
        testimonial = paginator.page(page)
    except EmptyPage:
        testimonial = paginator.page(1)
    except PageNotAnInteger:
        testimonial = paginator.page(1)
    except InvalidPage:
        testimonial = paginator.page(1)

    context = {'testimonial': testimonial, 'paginator': paginator}
    
    return render(request, 'dashboard/testimonials/testimonials.html', context)

@login_required(login_url='login')
def add_testimonials(request):
    member = ''
    user = request.user
    if user.is_admin == True:
        member = Team_Member.objects.all()
    elif user.is_team_member == True:
        member = Team_Member.objects.get(username=user)
    
    context = {'member': member}
    
    if request.method == 'POST':
        member_id = request.POST['member']
        member = Team_Member.objects.get(id=member_id)
        status = request.POST['status']
        
        testimonial = Testimonials.objects.create(
            team_member = member,
            person_name = request.POST['name'],
            person_designation = request.POST['designation'],
            opinion = request.POST['opinion'],
        )
        if status == 'Active':
            testimonial.is_active = True
        elif status == 'Inactive':
            testimonial.is_active = False
        
        if request.FILES.get('profile_picture'):
            testimonial.person_image = request.FILES.get('profile_picture')
        
        testimonial.save()
        messages.success(request, 'Create Testimonial Successfully!')
        return redirect('testimonials')
    
    return render(request, 'dashboard/testimonials/add_testimonials.html', context)

@login_required(login_url='login')
def update_testimonials(request, id):
    member = ''
    user = request.user
    if user.is_admin == True:
        member = Team_Member.objects.all()
    elif user.is_team_member == True:
        member = Team_Member.objects.get(username=user)
    
    testimonial = Testimonials.objects.get(id=id)
    context = {'member': member, 'testimonial': testimonial}
    
    if request.method == 'POST':
        member_id = request.POST['member']
        member = Team_Member.objects.get(id=member_id)
        
        profile_picture = request.FILES.get('profile_picture')
        status = request.POST['status']
        
        testimonial.team_member = member
        testimonial.person_name = request.POST['name']
        testimonial.person_designation = request.POST['designation']
        testimonial.opinion = request.POST['opinion']
        
        if status == 'Active':
            testimonial.is_active = True
        elif status == 'Inactive':
            testimonial.is_active = False
        
        if request.FILES.get('profile_picture'):
            if testimonial.person_image != 'default/personal_profile_tetimonial_icon.png':
                os.remove(testimonial.person_image.path)
            testimonial.person_image = request.FILES.get('profile_picture')
        
        testimonial.save()
        messages.success(request, 'Update Testimonial Successfully!')
        return redirect('testimonials')
        
    
    return render(request, 'dashboard/testimonials/update_testimonials.html', context)

@login_required(login_url='login')
def delete_testimonials(request, id):
    testimonial = Testimonials.objects.get(id=id)
    
    if testimonial.person_image != 'default/personal_profile_tetimonial_icon.png':
        os.remove(testimonial.person_image.path)
        
    testimonial.delete()
    messages.success(request, 'Delete Testimonial Successfully!')
    return redirect('testimonials')
# -------------Testimonials Saction End----------------


# def my_profile(request):
#     return render(request, 'dashboard/dashboard_home/my_profile.html')
