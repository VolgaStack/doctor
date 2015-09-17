from django import forms

class DoctorForm(forms.Form):
    name = forms.CharField(label='ФИО', max_length=200,)
    date = forms.DateField(label='Дата записи',)
 
    
