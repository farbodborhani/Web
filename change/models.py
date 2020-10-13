from django.db import models

class Change_picture(models.Model):

    image_page=models.ImageField(upload_to="change/images",default="")
