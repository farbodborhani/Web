from django.db import models

class MyWorkData(models.Model):

    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Number=models.CharField(max_length=100)
    Disc=models.TextField(default="")
    image=models.ImageField(upload_to='work/images',default="")
