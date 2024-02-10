from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField (max_length=100,default='',null = True)
    email = models.EmailField(max_length=100,default='',null = True)
    address = models.TextField(max_length=100)
    Mobile = models.BigIntegerField (default=1)

    def __str__(self):
        return self.name
