from django import forms
from .models import Contact, Booking

class Cform(forms.ModelForm):
    class Meta:
        model =  Contact
        fields = "__all__"

class Bform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['Name', 'Mobile_no']