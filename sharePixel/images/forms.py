from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets 
from .models import Images 

class ImagePostForm(forms.ModelForm): 

    class Meta: 
        model = 'Images'
        fields = (
            'title', 
            'url', 
            'description', 
        )

        widgets = {
            'url' : forms.HiddenInput, 
        }

    def clean_url(self): 
        url = self.cleaned_data['url']
        valid_extension = ['jpg','jpeg']
        extension = url.rsplit('.',1)[1].lower()
        if extension not in valid_extension: 
            raise ValidationError('Image provided extension not valid !!!')
        return url 

    