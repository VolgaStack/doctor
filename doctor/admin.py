from django.contrib import admin

from .models import Doctor, Appointment

class DoctorAdmin(admin.ModelAdmin):    
    list_display = ('name', 'specialization')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'app_date', 'client_name')
    list_filter = ['doctor']
    search_fields = ['app_date']

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
