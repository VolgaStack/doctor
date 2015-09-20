from django.contrib import admin

from .models import Doctor, Appointment, DoctorSpecs

class DoctorSpecsAdmin(admin.ModelAdmin):    
    list_display = ('spec_code', 'spec_name')

class DoctorAdmin(admin.ModelAdmin):    
    list_display = ('name', 'spec')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'app_date', 'client_name')
    list_filter = ['doctor']
    search_fields = ['app_date']

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(DoctorSpecs, DoctorSpecsAdmin)