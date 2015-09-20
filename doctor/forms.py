from django import forms
from .models import Doctor

DATE_FORMATS = [
'%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
'%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
'%m/%d/%Y %H:%M:%S',    # '10/25/2006 14:30:59'
'%m/%d/%Y %H:%M',       # '10/25/2006 14:30'
'%m/%d/%y %H:%M:%S',    # '10/25/06 14:30:59'
'%m/%d/%y %H:%M',       # '10/25/06 14:30'
'%d.%m.%Y %H:%M', 		# '22.08.2015 16:52' 
'%d.%m.%Y %H:%M:%S', 	# '22.08.2015 16:52:25'
'%d.%m.%y %H:%M', 		# '22.08.15 16:52' 
'%d.%m.%y %H:%M:%S']  	# '22.08.15 16:52:25'         

class AppointmentForm(forms.Form):
    name = forms.CharField(label='ФИО', max_length=200,)
    date_time = forms.DateTimeField(label='Дата и время:', input_formats=DATE_FORMATS)
    doctor = forms.ModelChoiceField(label='Врач:',queryset=Doctor.objects.all())
    
