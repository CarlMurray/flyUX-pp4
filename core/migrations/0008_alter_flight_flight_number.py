# Generated by Django 4.2.3 on 2023-08-04 18:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_flight_flight_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flight",
            name="flight_number",
            field=models.CharField(
                max_length=50,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Flight number must be in the format UX00000",
                        regex="UX\\d\\d\\d\\d\\d",
                    )
                ],
            ),
        ),
    ]