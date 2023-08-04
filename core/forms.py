from django import forms

class PassengerForm(forms.Form):
    first = forms.CharField(max_length=100)
    last = forms.CharField(max_length=100)

class TripContactForm(forms.Form):
    email = forms.EmailField(max_length=50)
