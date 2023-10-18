# Generated by Django 4.2.6 on 2023-10-18 13:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ships_manager_app", "0003_speed_load_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ship",
            name="year_of_built",
            field=models.PositiveIntegerField(
                blank=True,
                default=1900,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1900.0),
                    django.core.validators.MaxValueValidator(3000.0),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="speed",
            name="consumption_additional",
            field=models.FloatField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(20.0),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="speed",
            name="consumption_main",
            field=models.FloatField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(120.0),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="speed",
            name="speed_in_kn",
            field=models.FloatField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0.0),
                    django.core.validators.MaxValueValidator(100.0),
                ],
            ),
        ),
    ]