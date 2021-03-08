from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required 

# @func_name : base_render 
def base_render(request): 
    return render(request, 'base.html', {}) 


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


def required_page(request): 
    return render(request, 'registration/login.html', {})


@login_required 
def dashboard(request): 
    context = {}
    return render(request, 'account/dashboard.html', context) # render dashboard. 

    

