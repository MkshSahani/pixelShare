from django import forms
from django.forms import fields 
from .models import Profile 

class ProfileForm(forms.ModelForm): 

    class Meta: 
        model = Profile 
        fields = ('date_of_birth', 'photo') # field of forms. 

        