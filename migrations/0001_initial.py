# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('appointment_date', models.DateTimeField(verbose_name='date of appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('specialization', models.CharField(max_length=10, choices=[('S1', 'DOCTOR_SPEC_1'), ('S2', 'DOCTOR_SPEC_2'), ('S3', 'DOCTOR_SPEC_3')])),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(to='doctor.Doctor'),
        ),
    ]
