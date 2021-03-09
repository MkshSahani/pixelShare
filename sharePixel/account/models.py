from django.db import models
from django.conf import settings 


# class : Profile 
class Profile(models.Model): 
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)  
    date_of_birth = models.DateField(blank=True, null = True)
    photo = models.ImageField(blank=True, upload_to="profile_photos")


    def __str__(self): 
        return "profile of {self.user.username}" # show this string on admin. 
    
    