from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_index_page(request):
    return render(request, "mainsite/index.html")

def get_about_page(request):
    return render(request, "mainsite/about.html")

def get_moonwalks(request):
    return render(request, "mainsite/moonwalks.html")

def get_pinatas(request):
    return render(request, "mainsite/pinatas.html")

def get_faq_page(request):
    return render(request, "mainsite/faq.html")

def get_contact_page(request):
    return render(request, "mainsite/contact.html")