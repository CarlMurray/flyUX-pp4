# Generated by Django 4.2.3 on 2023-08-06 18:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_alter_booking_reference"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="reference",
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
