# Generated by Django 2.0.2 on 2018-02-27 01:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sdr', '0002_sdr_p_id'),
        ('data', '0004_auto_20180216_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='sdr_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sdr_id', to='sdr.Sdr'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 1, 57, 41, 782571, tzinfo=utc)),
        ),
    ]
