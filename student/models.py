from  django.db import models
class Studenttable(models.Model):
    name=models.CharField(max_length=30)
    contactno=models.IntegerField(unique=True)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=30)