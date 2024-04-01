from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Nombre', max_length=100, required=True)
    phone = forms.CharField(label= 'Télefono', required=False)
    email = forms.EmailField(label='Correo Electronico', max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea)
    term = forms.BooleanField(label='Terminos y Condiciones', required=True)

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'message', 'term']