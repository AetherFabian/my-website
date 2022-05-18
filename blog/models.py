from django.db import models
from django.db.models.fields import CharField, DateField
from django.db.models.fields.files import ImageField
import datetime

class Post(models.Model):
    title = CharField(max_length=200)
    description = models.TextField()
    image = ImageField(upload_to='blog/images')
    date = DateField(datetime.date.today)