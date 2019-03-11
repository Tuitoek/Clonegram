from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    return render(request,'landing.html')

def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request,'profile.html')

def home2(request):
    return render(request,'home2.html')    
