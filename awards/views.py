from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    allimages = "x"

    return render(request, 'homepage.html', {"images":allimages})
