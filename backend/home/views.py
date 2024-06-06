
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from email.header import Header
from django.core.mail import get_connection

from .forms import ContactForm, CareerContactForm
from .models import Contact, CareerContact

def submit_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('Form valid, send some data')
            subject = "site form"
            message = f"From: {form.cleaned_data['name']}<br>Email: {form.cleaned_data['email']}<br>Message: {form.cleaned_data['message']}"
            admin_emails = [email for name, email in settings.ADMINS]
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            # finish message creation
            messages.success(request, _('Message saved!'))
            print(f'{message=}')
            return redirect('/')
        else:
            print('Form NOT valid, can`t send data')
            messages.error(request, _('Error, form data not valid. Message not saved.'))
    else:
        print('Form new')
        form = ContactForm()
    # redirect user to home
    return redirect('/')


def submit_career_form(request):
    if request.method == 'POST':
        form = CareerContactForm(request.POST)
        if form.is_valid():
            print('Form valid, send some data')
            subject = "site form"
            message = f"From: {form.cleaned_data['name']}<br>Email: {form.cleaned_data['email']}<br>Message: {form.cleaned_data['message']}"
            admin_emails = [email for name, email in settings.ADMINS]
            CareerContact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )

            # finish message creation
            messages.success(request, _('Message saved!'))
            print(f'{message=}')
            return redirect('/')
        else:
            print('Form NOT valid, can`t send data')
            messages.error(request, _('Error, form data not valid. Message not saved.'))
    else:
        print('Form new')
        form = CareerContactForm()
    # redirect user to home
    return redirect('/')