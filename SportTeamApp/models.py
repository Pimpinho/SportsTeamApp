from django.db import models

# Create your models here.

class Team(models.Model):
    completeName = models.CharField(max_length=50)
    shortName = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    stadium = models.CharField(max_length=100)
    coach = models.CharField(max_length=50)
    president = models.CharField(max_length=50)
    foundationYear = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #shield = models.ImageField(upload_to='shields/')
    def __str__(self):
        return self.shortName

class Player(models.Model):
    completeName = models.CharField(max_length=50)
    shirtName = models.CharField(max_length=20, null=False)
    birthDate = models.DateField()
    position = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.shirtName
    

