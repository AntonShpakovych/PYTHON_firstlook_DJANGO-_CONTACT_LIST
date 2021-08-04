from django.db.models.base import Model
from add_contact.models import Contact
from django.forms import ModelForm, TextInput, NumberInput, EmailInput


class AddContactForms(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'sur_name', 'email', 'phone']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'sur_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Surname'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'phone': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone'
            })
        }
