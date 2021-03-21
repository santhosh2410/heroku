from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=10,default="")
    message=models.CharField(max_length=200,default="")

    def __str__(self):
        return self.name