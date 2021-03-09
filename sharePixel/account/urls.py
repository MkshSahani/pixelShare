from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView 
from .views import (
                    base_render, 
                    required_page, 
                    dashboard, 
                    register_user, 
                    user_login, 
                    edit_profile
                )


urlpatterns = [
    path('base/',base_render, name="BaseRender"), # account urls. 
    path('login/', user_login, name="login"), 
    path('logout/', LogoutView.as_view(template_name="registration/logout.html"), name="logout"), 
    path('required_page/', required_page, name="RequiredPage"), 
    path('signup/', register_user, name="signup"), 
    path('edit/', edit_profile, name="edit"), 
    path('',dashboard, name="dashboard"), 
    
]


