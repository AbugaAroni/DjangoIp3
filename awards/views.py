from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Profile, Project, Rating
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import NewProjectForm, NewProfileForm, NewRatingsForm
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer, ProfileSerializer

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

            average_rating = ((Ratinz.design + Ratinz.content + Ratinz.usablity)/3)
            Existing_rating = projects.score
            newcount = projects.ratedcount + 1
            new_rating = (Existing_rating + (average_rating-Existing_rating)/newcount)
            projects.update_project(projects.id,new_rating)

            return HttpResponseRedirect(reverse("view_project", args=[projects.id]))
    else:
        form = NewRatingsForm()
    return render(request, 'singleproject.html', {"form": form, "project":projects, "ratingz":ratingz})

def search_results(request):

    if 'project_search' in request.GET and request.GET["project_search"]:
        search_term = request.GET.get("project_search")
        searched_projects = Project.search_by_project(search_term)
        message = f"{search_term}"

        return render(request, 'searchresult.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searchresult.html',{"message":message})

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
