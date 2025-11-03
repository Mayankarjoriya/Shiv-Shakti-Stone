from django import forms
from .models import ContactMessage, QuoteRequest

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'mobile', 'message']

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['product', 'name', 'email', 'mobile', 'address', 'message']
