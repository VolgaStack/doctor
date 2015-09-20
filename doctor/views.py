from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .kdm_utils import CheckDatetime
from .forms import AppointmentForm
from .models import Appointment

def index(request):
    curr_date = timezone.now()
    form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data.get('name', None)
        date_time = form.cleaned_data.get('date_time', None)
        doctor = form.cleaned_data.get('doctor', None)
		
        # creating list with dates of existing appointments
        invalid_date_list = Appointment.objects.values_list('app_date', flat=True).filter(app_date__gt=curr_date, doctor=doctor)
        if CheckDatetime(curr_date, date_time, invalid_date_list):	
            app = Appointment(app_date=date_time ,doctor=doctor, client_name=name)
            app.save()
            return HttpResponse("Запись к врачу успешно зарегистрирована!")
		
    else:
	    form = AppointmentForm()
		
    return render(request, 'doctor/index.html', { 'form': form, })
