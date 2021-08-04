from django.shortcuts import render
from contact_list import *
from add_contact.models import *
from django.views.generic import ListView


class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list/contact-list.html'
    context_object_name = 'contact'
