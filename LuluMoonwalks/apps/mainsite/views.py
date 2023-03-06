import re
from .forms import contact_us
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail

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
        Fields in the form:
            - Full Name (fullname)
            - Email (email)
            - Phone (phone)
            - Message (message)
    """
    contact_form = contact_us(request.POST or None)

    if request.method == "POST":
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            phone = contact_form.cleaned_data['phone_number']
            message = contact_form.cleaned_data['message']

        # Construct the email message
            subject = f"New Contact Form Submission from {name}"
            message_text = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"
            from_email = settings.DEFAULT_FROM_EMAIL # bmoonwalkers@gmail.com
            recipient_list = ['', '']  # replace with your own email address

            for key in request.POST.keys():
                print(f"{key}: {request.POST.get(key)}")

            # This should be the line of code that sends the email
            send_mail(subject, message_text, from_email, recipient_list)

            messages.success(request, "Form submission successful")

    context = {
        "form": contact_form,
        "method": request.method
    }

    return render(request, "mainsite/contact.html", context)






