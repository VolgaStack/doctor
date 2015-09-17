from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .forms import DoctorForm
from .models import Appointment

def index(request):
    form = DoctorForm(request.POST or None)
    context = { 'form': form, }
    template = 'doctor/index.html'
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data.get('name', None)
        date = form.cleaned_data.get('date', None)
        doctor = form.cleaned_data.get('doctor', None)
		
    else:
	    form = DoctorForm()
		
    return render(request, template, context)
	
	
def thanks(request):
    return HttpResponse("Спасибо за использование нашей клиники")
