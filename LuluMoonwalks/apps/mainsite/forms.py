from django import forms

class contact_us(forms.Form):
    name = forms.CharField(label="Full name", max_length=100,
                           widget=forms.TextInput(attrs={
                               "class": "form-control",
                               "name": "fullname",
                               "id": "name",
                               "type": "text",
                               "placeholder": "Enter your name..."
                           }))

    email = forms.EmailField(label="Email address", max_length=50,
                             widget=forms.EmailInput(attrs={
                                "class": "form-control",
                                "name": "email",
                                "id": "email",
                                "type": "email",
                                "placeholder": "name@example.com"
                             }))

    phone_number = forms.CharField(label="Phone number", max_length=17,
                            widget=forms.TextInput(attrs={
                                "class": "form-control",
                                "name": "phone",
                                "id": "phone",
                                "type": "tel",
                                "placeholder": "123-456-7890"
                            }))

    message = forms.CharField(label="Message",
                              widget=forms.Textarea(attrs={
                                "class": "form-control",
                                "name": "message",
                                "id": "message",
                                "type": "text",
                                "placeholder": "Enter your message here..."
                              }))