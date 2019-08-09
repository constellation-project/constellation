from django.contrib.auth.models import User
from django.db import models


class Member(User):
    address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=31)

class Organization(User):
    address = models.CharField(max_length=255)
    manager = models.ForeignKey(Member, on_delete=models.PROTECT, related_name='organizations')
    members = models.ManyToManyField(Member)

class Administrator(Member):
    pgp = models.CharField(max_length=40)

class Membership(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT, related_name='memberships')
    date_start = models.DateField()
    date_end = models.DateField(null=True)
