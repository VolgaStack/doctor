# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='client_name',
            field=models.CharField(default='No data', max_length=200),
            preserve_default=False,
        ),
    ]
