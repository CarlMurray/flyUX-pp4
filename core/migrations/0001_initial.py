# Generated by Django 4.2.3 on 2023-07-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Airport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("iata", models.CharField(max_length=3)),
                ("locality", models.CharField(max_length=50)),
                ("region", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=50)),
            ],
        ),
    ]
