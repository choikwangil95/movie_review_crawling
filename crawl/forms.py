# forms.py

from django import forms 
from .models import Moviedata

class ReviewSearchForm(forms.ModelForm): 
    class Meta:
        model = Moviedata
        fields = ['title']