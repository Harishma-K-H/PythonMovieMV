# for update
from django import forms
from .models import movies
class MovieForms(forms.ModelForm):
    class Meta:
        model=movies
        fields=['name','des','year','img']
