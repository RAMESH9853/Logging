# "do" import forms

from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(label = 'Enter Your Name ',required = True)
    contact_emial = forms.CharField(label = 'Enter Your E-mail ',required = True)
    contact_message = forms.CharField(label = 'Your Message ',required = True, widget = forms.Textarea)
