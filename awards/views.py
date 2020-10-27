from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Rating
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
def home(request):
    allprojects = Project.objects.all()
    return render(request, 'homepage.html', {"projects":allprojects})

@login_required(login_url='/accounts/login/')
def view_user(request, userid):
    current_user=User.objects.get(id=userid)
    projects = Project.objects.filter(Q(creator=current_user))
    profiles = Profile.objects.get(username=current_user)

    return render(request, 'viewuser.html', {"projects":projects,  "profiles":profiles})
