from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Index.html')

def LoginScout(request):
    return render(request, 'LoginScout.html')

def LoginSeeker(request):
    return render(request, 'LoginSeeker.html')

def RegisterScout(request):
    return render(request, 'RegisterScout.html')

def RegisterSeeker(request):
    return render(request, 'RegisterSeeker.html')
