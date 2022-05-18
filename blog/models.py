from django.db import models
from django.forms import CharField, DateField, ImageField
import datetime

class Posts(models.Model):
    title = CharField(max_length=200)
    description = models.TextField()
    image = ImageField(upload_to='blog/images')
    date = DateField(datetime.date.today)