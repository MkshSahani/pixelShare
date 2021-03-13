from django import forms
from django.forms import fields 
from .models import Images  

class ImageForms(forms.ModelForm): 
    
    class Meta: 
        model = Images 
        fields = (
            'title', 
            'img', 
            'description'
        )

    