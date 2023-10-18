from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Ship(models.Model):
    name = models.CharField(max_length=200)
    year_of_built = models.PositiveIntegerField(null=True, blank=True,
                                                default=2000, validators=[
                                                    MinValueValidator(1900.0),
                                                    MaxValueValidator(3000.0)])


class Speed(models.Model):
    LOAD_STATUS_CHOICES = [
        ('ballast', 'Ballast'),
        ('laden', 'Laden'),
    ]
    name = models.CharField(max_length=200)
    load_status = models.CharField(
        max_length=10, choices=LOAD_STATUS_CHOICES)
    speed_in_kn = models.FloatField(
        default=0)
    consumption_main = models.FloatField(
        default=0)
    consumption_additional = models.FloatField(
        default=0)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE,
                             blank=True, null=True)
