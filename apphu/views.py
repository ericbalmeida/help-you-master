from django.shortcuts import render

def home(request):
    return render(request, 'apphu/home.html')
# Create your views here.
