from django.db import models

# Create your models here.
class Country(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class State(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country)
    def __str__(self):
        return self.name