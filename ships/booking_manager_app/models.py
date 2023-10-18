from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=240)
    address = models.CharField(max_length=340)


class Booking(models.Model):
    cargo_name = models.CharField(max_length=40)
    cargo_quantity = models.PositiveIntegerField()
    cargo_quantity_allowance = models.PositiveIntegerField()
    load_port = models.CharField(max_length=40)
    discharge_port = models.CharField(max_length=40)
    date_open = models.DateField()
    date_close = models.DateField()
    account = models.ForeignKey(
        Account, on_delete=models.DO_NOTHING, blank=True, null=True
    )
