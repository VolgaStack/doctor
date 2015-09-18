from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .kdm_utils import check_datetime,combine_datetime
from .forms import AppointmentForm
from .models import Appointment

def index(request):
    curr_date = datetime.date(timezone.now())
    form = AppointmentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        myName = form.cleaned_data.get('name', None)
        myTime = form.cleaned_data.get('time', None)       
        myDate = form.cleaned_data.get('date', None)
        myDoctor = form.cleaned_data.get('doctor', None)
		
        invalid_date_list = Appointment.objects.values_list('app_date', flat=True).filter(app_date__gt=curr_date, doctor=myDoctor)
        if check_datetime(curr_date, myDate, myTime, invalid_date_list):
            myDateTime = combine_datetime(myDate, myTime)		
            app = Appointment(app_date=myDateTime ,doctor=myDoctor, client_name=myName)
            app.save()

            return HttpResponse("Запись к врачу успешно зарегистрирована!")
		
    else:
	    form = AppointmentForm()
		
    return render(request, 'doctor/index.html', { 'form': form, })
