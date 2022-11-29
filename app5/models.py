from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
class images(models.Model):
    name1=models.CharField(max_length=100)
    image1=models.ImageField(upload_to='pics')
    disc=models.TextField()


