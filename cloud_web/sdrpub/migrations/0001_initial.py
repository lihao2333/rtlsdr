# Generated by Django 2.0.2 on 2018-02-27 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sdr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('name', models.CharField(max_length=20)),
                ('loc_x', models.FloatField(max_length=10)),
                ('loc_y', models.FloatField(max_length=10)),
            ],
        ),
    ]
