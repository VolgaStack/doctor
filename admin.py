from django.contrib import admin

from .models import Doctor
from .models import Appointment

class DoctorAdmin(admin.ModelAdmin):
    fields = ['name', 'specialization']
    list_display = ('specialization', 'name')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'appointment_date')

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
