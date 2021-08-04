from add_contact.models import Contact
from django.shortcuts import render, redirect
from .forms import *


def add_contact(requests):
    error = ''
    if requests.method == 'POST':
        form = AddContactForms(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('contact-list')
        else:
            error = 'Form uncorrect!!!'
    form = AddContactForms()

    data = {
        'form': form,
        'error': error
    }

    return render(requests, 'add_contact/add_contact.html', data)
