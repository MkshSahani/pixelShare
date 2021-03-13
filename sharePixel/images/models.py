from django.db import models
from django.conf import settings 
from django.utils.text import slugify

class Images(models.Model): 

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_images", on_delete=models.CASCADE) 
    title = models.CharField(max_length=200) 
    img = models.ImageField(upload_to='user_images') 
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    user_liked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_like', blank=True)
    

    def save(self, *args, **kwargs): 
        if not self.slug: 
            self.slug = slugify(self.title)
            super(Images, self).save(*args, **kwargs)

    def __str__(self): 
        return self.title 

    