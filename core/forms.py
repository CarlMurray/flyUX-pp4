from django import forms


class PassengerForm(forms.Form):
    """ 
    Form for passenger details on passenger details page.
    """
    first = forms.CharField(max_length=100)
    last = forms.CharField(max_length=100)


class TripContactForm(forms.Form):
    """ 
    Form for email address on passenger details page.
    """
    email = forms.EmailField(max_length=50)
