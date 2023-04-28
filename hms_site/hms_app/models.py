from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.TextField()
    address = models.TextField()
    rollno = models.IntegerField()
    mobileno = models.BigIntegerField()
    email = models.TextField()
    password = models.TextField()
    is_hosteller = models.TextField(default='No')
    


