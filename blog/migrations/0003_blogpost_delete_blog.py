# Generated by Django 4.2.3 on 2023-08-18 21:20

from django.db import migrations, models
import markdownfield.models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_blog_content_rendered_alter_blog_content"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
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
                ("title", models.CharField(max_length=120)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "content",
                    markdownfield.models.MarkdownField(
                        rendered_field="content_rendered"
                    ),
                ),
                ("content_rendered", markdownfield.models.RenderedMarkdownField()),
                ("cover_image", models.ImageField(upload_to="blog_images/")),
            ],
        ),
        migrations.DeleteModel(
            name="Blog",
        ),
    ]
