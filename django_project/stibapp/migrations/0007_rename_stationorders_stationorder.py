# Generated by Django 4.1.3 on 2022-11-18 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stibapp', '0006_remove_line_stations_stationorders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StationOrders',
            new_name='StationOrder',
        ),
    ]