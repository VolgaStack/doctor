from django import forms
from .models import Doctor

class DoctorForm(forms.Form):
    name = forms.CharField(label='ФИО', max_length=200,)
    date = forms.DateField(label='Дата записи',)
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())
 
    
