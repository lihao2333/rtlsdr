# Generated by Django 2.0.2 on 2018-02-27 06:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20180227_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 6, 31, 32, 999878, tzinfo=utc)),
        ),
    ]