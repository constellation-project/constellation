from django.db import models


class BuildingGroup(models.Model):
    name = models.SlugField()
    full_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Building(models.Model):
    group = models.ForeignKey(BuildingGroup, null=True, blank=True, on_delete=models.SET_NULL, related_name='buildings')
    number = models.SlugField()
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.number}@{self.group.name}"

    class Meta:
        unique_together = ('group', 'number')

class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='rooms')
    number = models.SlugField()
    occupant = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL, related_name='room')

    def __str__(self):
        return f"{self.building.number}{self.number}@{self.building.group.name}"

    class Meta:
        unique_together = ('building', 'number')
