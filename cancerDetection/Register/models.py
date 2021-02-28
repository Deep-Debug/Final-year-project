from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    emailid = models.EmailField(max_length=20,primary_key=True)
    password=models.CharField(max_length=30)