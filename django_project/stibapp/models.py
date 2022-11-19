# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


class User(models.Model):
    pseudo = models.fields.CharField(max_length=25)
    password = models.fields.CharField(max_length=20)
    isadmin = models.fields.BooleanField(default=False)

    def __str__(self):
        return self.pseudo


class Admin(models.Model):
    pseudo = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.fields.CharField(max_length=20)

    def __str__(self):
        return self.pseudo.pseudo


class Station(models.Model):
    station_name = models.fields.CharField(max_length=50)
    locality = models.fields.CharField(max_length=50)

    def __str__(self):
        return self.station_name


class Line(models.Model):
    class Category(models.TextChoices):
        TRAM = 'TRAM'
        BUS = 'BUS'
        METRO = 'METRO'

    direction = models.fields.CharField(max_length=50)
    number = models.fields.PositiveIntegerField()
    category = models.fields.CharField(choices=Category.choices, max_length=5)

    def __str__(self):
        return 'Ligne ' + str(self.number) + ' Direction: ' + self.direction


class StationOrder(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    order = models.fields.PositiveIntegerField()

    def __str__(self):
        direction, station, order = self.line.direction, self.station.station_name, str(self.order)
        return ' Ligne ' + direction + ' | Station : ' + station + ' | Station no.' + order


class Control(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)

    def __str__(self):
        number, station_name = self.line.number, self.station.station_name
        return "Controle a la station '" + station_name + "' sur la ligne " + str(number)

