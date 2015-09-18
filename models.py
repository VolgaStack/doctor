from django.db import models

DOC_SPECS = (
        ('somecode01', 'Кардиохирург'),
        ('somecode02', 'Нейрохирург'),
        ('somecode03', 'Косметолог'),
)

class Doctor(models.Model):   
    specialization = models.CharField(max_length=10, choices=DOC_SPECS)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.specialization)

class Appointment(models.Model):
    app_date = models.DateTimeField('Date and Time')
    doctor = models.ForeignKey(Doctor)
    client_name = models.CharField(max_length=200)

    def __str__(self):
        return 'Дата и время: {0}/n врач: {1}'.format(self.app_date, self.doctor)
