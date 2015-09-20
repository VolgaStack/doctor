from django.db import models

class DoctorSpecs(models.Model):
    spec_code = models.CharField(max_length=10)
    spec_name = models.CharField(max_length=100)

    def __str__(self):
        return '{0}'.format(self.spec_name)

class Doctor(models.Model):
    spec = models.ForeignKey(DoctorSpecs)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.spec)
		
class Appointment(models.Model):
    app_date = models.DateTimeField()
    doctor = models.ForeignKey(Doctor)
    client_name = models.CharField(max_length=200)

    def __str__(self):
        return 'Дата и время: {0} врач: {1}'.format(self.app_date, self.doctor)