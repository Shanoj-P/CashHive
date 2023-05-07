from django.db import models

from homeApp.models import District, Branches


# Create your models here.
class Account(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender')
    )
    Accunt_type = (
        ('S', 'Savings'),
        ('C', 'Current'),

    )

    name = models.CharField(max_length=250)
    DOB = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.IntegerField()
    email = models.CharField(max_length=250)
    address = models.CharField(max_length=300)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    account = models.CharField(max_length=1, choices=Accunt_type)
    cc = models.BooleanField()
    db = models.BooleanField()
    cb = models.BooleanField()

    def __int__(self):
        return '{}'.format(self.name)
