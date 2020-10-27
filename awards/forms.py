from .models import Project, Profile
from django import forms

#......
class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['creator', 'score']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']
