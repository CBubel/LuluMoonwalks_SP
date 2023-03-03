import re

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import contact_us

# Create your views here.
def get_index_page(request):
    context = {
        "value": "1"
    }
    return render(request, "mainsite/index.html", context)

def get_about_page(request):
    return render(request, "mainsite/about.html")

def get_moonwalks_page(request):
    return render(request, "mainsite/moonwalks.html")

def get_pinatas_page(request):
    return render(request, "mainsite/pinatas.html")

def get_faq_page(request):
    return render(request, "mainsite/faq.html")

def get_success_page(request):
    return render(request, "mainsite/success-page.html")

def get_test_page(request):
    return render(request, "mainsite/test.html")

def get_contact_page(request):
    """
    Here, we would have to identify a way to send the contact information that was given to us, to an email address
    """
    contact_form = contact_us(request.POST or None)

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

        # After submitting, the user should be taken to a simple success page
        if contact_form.is_valid():
            messages.success(request, "Form submission successful")

    context = {
        "form": contact_form,
        "method": request.method
    }

    return render(request, "mainsite/contact.html", context)






