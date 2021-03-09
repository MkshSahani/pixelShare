from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, logout, login 
from .forms import ProfileForm 

# @func_name : base_render 
def base_render(request): 
    return render(request, 'base.html', {}) 


# @func_name : user_login 
def user_login(request): 
    context = {}
    context['login_failed'] = False 
    if request.method == "POST": 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) # authenticate user. 
        if user is not None: 
            if user.is_active: 
                login(request, user) # start session with user. 
                return redirect('/account/') # redirect to home page. 
        else:
            context['login_failed'] = True 
            return render(request, 'registration/login.html', context) # login faild redirect to login page, with warning. 
    else: 
        return render(request, 'registration/login.html', context) # render login page.  


# @func_name : register_user. 
def register_user(request): 
    context = {} # context. 
    context['new_user_added'] = False 
    if request.method == "POST": 
        username = request.POST.get('username')
        password = request.POST.get('password')
        email_address = request.POST.get('emailAddress')
        print(username, password, email_address) # print data. 
        new_user = User.objects.create_user(username=username, password=password, email=email_address) # addnew user.  
        context['new_user_added'] = True 
        context['new_user'] = new_user # store data of new_user. 
        return render(request, 'registration/signup.html', context) # render sucess registration. 
    else: 
        return render(request, 'registration/signup.html', context) # render singup page. 


# @func_name : edit_profile. 
def edit_profile(request): 
    context = {}
    context['profile_updated'] = False 
    if request.method == "POST": 
        profile_forms_data = ProfileForm(instance=request.user.profile, data = request.POST, file = request.FILES)
        if profile_forms_data.is_valid(): 
            profile_forms_data.save()
            context['profile_updated'] = True 
            return render(request, 'account/edit.html', context) 
    else: 
        profile_form = ProfileForm(instance=request.user.profile)
        context['profile_form'] = profile_form
        return render(request, 'account/edit.html', context)


def required_page(request): 
    return render(request, 'registration/login.html', {})


@login_required 
def dashboard(request): 
    context = {}
    return render(request, 'account/dashboard.html', context) # render dashboard. 

    

