from django import forms

class NameForm(forms.Form):
    firstName = forms.CharField(label="Your name", max_length=100)