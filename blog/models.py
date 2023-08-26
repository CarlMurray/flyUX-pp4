from django.db import models
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    content = MarkdownField(
        rendered_field="content_rendered", validator=VALIDATOR_STANDARD
    )
    content_rendered = RenderedMarkdownField()
    cover_image = models.ImageField(upload_to="blog_images/")

    def __str__(self):
        return self.title
