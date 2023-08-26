# Generated by Django 4.2.3 on 2023-07-09 17:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_remove_aircraft_ac_type_aircraft_aircraft_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="airport",
            name="iata",
            field=models.CharField(
                max_length=3,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="IATA code should be three uppercase letters",
                        regex="[A-Z]+",
                    )
                ],
                verbose_name="IATA code",
            ),
        ),
    ]
