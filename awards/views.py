from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Rating
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import NewProjectForm, NewProfileForm, NewRatingsForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(request):
    allprojects = Project.objects.all()
    return render(request, 'homepage.html', {"projects":allprojects})

@login_required(login_url='/accounts/login/')
def view_user(request, userid):
    current_user=User.objects.get(id=userid)
    projects = Project.objects.filter(Q(creator=current_user))
    try:
        profiles = Profile.objects.get(username=current_user)
    except Profile.DoesNotExist:
        profiles = ""

    return render(request, 'viewuser.html', {"projects":projects,  "profiles":profiles})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            newproject = form.save(commit=False)
            newproject.creator = current_user
            newproject.save()
        return redirect(profile)

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user=request.user
    projects = Project.objects.filter(Q(creator=current_user))
    try:
        profiles = Profile.objects.get(username=current_user)
    except Profile.DoesNotExist:
        profiles = ""

    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            Profilez = form.save(commit=False)
            Profilez.username = current_user
            Profilez.save()
        return redirect(profile)

    else:
        form = NewProfileForm()
    return render(request, 'accounts/profile.html', {"form": form, "projects":projects,  "profiles":profiles})

@login_required(login_url='/accounts/login/')
def view_project(request, projectid):
    current_user=request.user
    projects = Project.objects.get(id=projectid)
    try:
        ratingz = Rating.objects.get(userid=current_user, projectid = projects)
    except Rating.DoesNotExist:
        ratingz = ""

    if request.method == 'POST':
        form = NewRatingsForm(request.POST, request.FILES)
        if form.is_valid():
            Ratinz = form.save(commit=False)
            Ratinz.userid = current_user
            Ratinz.projectid = projects
            Ratinz.save()

        return render(request,'singleproject.html', {"form": form, "project":projects, "ratingz":ratingz})

    else:
        form = NewRatingsForm()
    return render(request, 'singleproject.html', {"form": form, "project":projects, "ratingz":ratingz})
