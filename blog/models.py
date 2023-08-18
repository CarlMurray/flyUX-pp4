from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title
