from django import forms
from django.forms import DateInput

from .models import Registration, contact


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"    # it will display all the fields in the form except default fields like id and registrationtime
        widgets = {"password":forms.PasswordInput(),"dateofbirth":DateInput()}    # additional features of the fields
        labels = {"gender":"Select Gender","location":"Provide Location"}  #using this, we can change label name in the form
        #exclude = {"gender"}       #using this, we can hide the fields in the form

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = "__all__"
        labels = {"fullname":"Enter Name","dateofbirth":"brand","email":"Enter Email","contact":'Type of product'}

