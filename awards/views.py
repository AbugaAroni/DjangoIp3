from django.shortcuts import render

# Create your views here.
def home(request):
    allimages = "x"

    return render(request, 'homepage.html', {"images":allimages})
