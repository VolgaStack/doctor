from django import forms
from .models import Doctor

class AppointmentForm(forms.Form):
    name = forms.CharField(label='ФИО', max_length=200,)
    date = forms.DateField(label='Дата записи',)
    time = forms.TimeField(label='Время записи',widget=forms.TimeInput(format='%H:%M'))   
    doctor = forms.ModelChoiceField(label='Врач:',queryset=Doctor.objects.all())
 
    
