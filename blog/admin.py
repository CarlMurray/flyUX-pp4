from django.contrib import admin
from .models import *

# Register your models here.
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'date', 'content', 'cover_image')

admin.site.register(BlogPost)