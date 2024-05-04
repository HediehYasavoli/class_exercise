from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request , 'root/index.html')


def contact(request):
    return render(request , 'root/contact.html')


def about(request):
    return render(request , 'root/about.html')