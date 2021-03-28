from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home_page, name="Image_app_home_page"),
]
