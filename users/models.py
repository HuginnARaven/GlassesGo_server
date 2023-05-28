from django.contrib.auth.models import AbstractUser
from django.db import models

from glasses.models import *


class UserAccount(AbstractUser):
    pass


class OrderPremade(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    street = models.CharField(max_length=255, null=False)
    glasses = models.ForeignKey(PremadeGlasses, on_delete=models.CASCADE, null=False)


class OrderCustom(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    street = models.CharField(max_length=255, null=False)
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE, null=False)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=False)
    material_color = models.ForeignKey(MaterialColor, on_delete=models.CASCADE, null=False)
    lens = models.ForeignKey(Lens, on_delete=models.CASCADE, null=False)
    lens_color = models.ForeignKey(LensColor, on_delete=models.CASCADE, null=False)