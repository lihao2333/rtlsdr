# Generated by Django 2.0.2 on 2018-02-16 17:04

import data.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='data',
            field=models.FileField(default='qwe', upload_to=data.models.user_directory_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 16, 17, 4, 43, 914155, tzinfo=utc)),
        ),
    ]
