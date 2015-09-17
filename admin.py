from django.contrib import admin

from .models import Doctor
from .models import Appointment

class DoctorAdmin(admin.ModelAdmin):    
    list_display = ('name', 'specialization')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'appointment_date', 'client_name')
    list_filter = ['doctor', 'appointment_date']
    search_fields = ['doctor']

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
