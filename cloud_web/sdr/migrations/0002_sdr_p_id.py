# Generated by Django 2.0.2 on 2018-02-16 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdr',
            name='p_id',
            field=models.IntegerField(default=9999, max_length=6),
            preserve_default=False,
        ),
    ]
