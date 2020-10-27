from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Rating
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    allprojects = Project.objects.all()
    return render(request, 'homepage.html', {"projects":allprojects})
