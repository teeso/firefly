# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0007_vehicle_route_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beacon',
            name='registration_number',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='registration_number',
            field=models.CharField(max_length=30, null=True, verbose_name='registration number associated'),
        ),
    ]