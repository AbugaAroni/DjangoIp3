from .models import Project, Profile, Rating
from django import forms

#......

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['creator', 'score', 'ratedcount']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']

class NewRatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['userid', 'projectid']
