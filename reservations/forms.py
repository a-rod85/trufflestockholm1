from django import forms
from django.forms import fields
from .models import Reservation

class ReserveTableForm(form.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'