from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.name}"


class District(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class City(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete = models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Village(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete = models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete = models.CASCADE)
    pincode = models.CharField(max_length=6)
    villageType = models.CharField(max_length=6, null=True)
    deliveryStatus = models.TextField(null=True)
    divisionName = models.CharField(max_length=30, null=True)
    regionName = models.CharField(max_length=30, null=True)
    circleName = models.CharField(max_length=30, null=True)
    telephone = models.CharField(max_length=12, null=True)
    relatedSuboffice = models.CharField(max_length=30, null=True)
    relatedHeadoffice = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.name}{self.pincode}{self.villageType}{self.deliveryStatus}{self.divisionName}{self.regionName}{self.circleName}{self.telephone}{self.relatedSuboffice}{self.relatedHeadoffice}"