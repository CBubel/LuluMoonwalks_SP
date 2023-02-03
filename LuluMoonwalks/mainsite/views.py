from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_home_page(request):
    return render(request, "mainsite/home.html")

def get_moonwalks(request):
    return render(request, "mainsite/moonwalks.html")

def get_pinatas(request):
    return render(request, "mainsite/pinatas.html")