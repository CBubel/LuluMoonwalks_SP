from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_index_page(request):
    return render(request, "mainsite/index.html")

def get_about_page(request):
    return render(request, "mainsite/about.html")

def get_moonwalks_page(request):
    return render(request, "mainsite/moonwalks.html")

def get_pricing_page(request):
    return render(request, "mainsite/pricing.html")

def get_pinatas_page(request):
    return render(request, "mainsite/pinatas.html")

def get_faq_page(request):
    return render(request, "mainsite/faq.html")

def get_contact_page(request):
    """
    Here, we would have to identify a way to send the contact information that was given to us, to an email address
    """
    if request.method == "POST":
        """
        Fields in the form:
            - Full Name (fullname)
            - Email (email)
            - Phone (phone)
            - Message (message)
        """
        for key in request.POST.keys():
            print(f"{key}: {request.POST.get(key)}")

    return render(request, "mainsite/contact.html")