from django.db import models

class Admintable(models.Model):
    name=models.CharField(max_length=30)
    pas=models.CharField(max_length=30)

class Scheduletable(models.Model):
    name=models.CharField(max_length=30,unique=True)
    faculty=models.CharField(max_length=30)
    date=models.DateField()
    fee=models.IntegerField()
    duration=models.TimeField()
