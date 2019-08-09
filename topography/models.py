from django.db import models


class BuildingGroup(models.Model):
    name = models.CharField(max_length=255)

class Building(models.Model):
    group = models.ForeignKey(BuildingGroup, null=True, on_delete=models.SET_NULL, related_name='buildings')
    number = models.CharField(max_length=31)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    class Meta:
        unique_together = ('group', 'number')

class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='rooms')
    number = models.CharField(max_length=31)
    occupant = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL, related_name='room')

    class Meta:
        unique_together = ('building', 'number')
