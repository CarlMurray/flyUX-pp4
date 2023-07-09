# Generated by Django 4.2.3 on 2023-07-09 17:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_aircraft_flight"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="aircraft",
            name="ac_type",
        ),
        migrations.AddField(
            model_name="aircraft",
            name="aircraft_type",
            field=models.CharField(
                choices=[
                    ("b737-700", "B737-700"),
                    ("b737-600", "B737-600"),
                    ("a321-100", "A321-100"),
                    ("a321-200", "A321-200"),
                ],
                default=1,
                max_length=50,
                verbose_name="Aircraft type",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="airport",
            name="iata",
            field=models.CharField(
                max_length=3,
                validators=[
                    django.core.validators.RegexValidator(
                        message="IATA code should be three uppercase letters",
                        regex="[A-Z]+",
                    )
                ],
                verbose_name="IATA code",
            ),
        ),
        migrations.AlterField(
            model_name="airport",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Airport name"),
        ),
        migrations.AlterField(
            model_name="flight",
            name="arr_time",
            field=models.DateTimeField(verbose_name="Arrival time"),
        ),
        migrations.AlterField(
            model_name="flight",
            name="dep_time",
            field=models.DateTimeField(verbose_name="Departure time"),
        ),
        migrations.AlterField(
            model_name="flight",
            name="flight_number",
            field=models.CharField(
                max_length=50,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Flight number must be in the format UX000",
                        regex="UX[0-9]+",
                    )
                ],
            ),
        ),
    ]
