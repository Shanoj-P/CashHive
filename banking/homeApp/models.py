from django.db import models

# Create your models here.
class District(models.Model):
    name = models.TextField(max_length=250, unique=True)
    link = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)

    def __int__(self):
        return '{}'.format(self.name)

class Branches(models.Model):
    branchName = models.TextField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    Tdistrict = models.ForeignKey(District, on_delete=models.CASCADE)

    class Meta:
        ordering = ('branchName',)

    def __int__(self):
        return '{}'.format(self.branchName)

