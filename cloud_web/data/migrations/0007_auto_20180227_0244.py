# Generated by Django 2.0.2 on 2018-02-27 02:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20180227_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 2, 44, 41, 746495, tzinfo=utc)),
        ),
    ]