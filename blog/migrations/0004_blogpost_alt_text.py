# Generated by Django 4.2.3 on 2023-08-26 21:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_blogpost_delete_blog"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="alt_text",
            field=models.CharField(blank=True, default="", max_length=120, null=True),
        ),
    ]