from django.db import models

class Doctor(models.Model):
    SPECS = (
        ('S1', 'DOCTOR_SPEC_1'),
        ('S2', 'DOCTOR_SPEC_2'),
        ('S3', 'DOCTOR_SPEC_3'),
        )
    specialization = models.CharField(max_length=10, choices=SPECS)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{0}, specs: {1}'.format(self.name, self.specialization)

class Appointment(models.Model):
    appointment_date = models.DateTimeField('date of appointment')
    doctor = models.ForeignKey(Doctor)

    def __str__(self):
        return 'time: {0} doctor: {1}'.format(self.appointment_date, self.doctor)
