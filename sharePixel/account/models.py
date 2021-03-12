from django.db import models
from django.conf import settings 


# class : Profile 
class Profile(models.Model): 
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)  
    email_address = models.EmailField(blank=True) # email field.s 
    photo = models.ImageField(upload_to="profile_photos/", blank=True)


    def __str__(self): 
        return f"profile of { self.user.username }" # show this string on admin. 
    
    