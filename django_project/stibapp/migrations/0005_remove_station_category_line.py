# Generated by Django 4.1.3 on 2022-11-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stibapp', '0004_station'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='category',
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(max_length=50)),
                ('number', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('TRAM', 'Tram'), ('BUS', 'Bus'), ('METRO', 'Metro')], max_length=5)),
                ('stations', models.ManyToManyField(to='stibapp.station')),
            ],
        ),
    ]
