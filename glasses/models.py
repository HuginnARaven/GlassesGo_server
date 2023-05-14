from django.db import models


class Frame(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False)
    photo_url = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.name}"


class Lens(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False)

    frame = models.ForeignKey(Frame, on_delete=models.CASCADE, null=False, related_name="frame_lens")

    def __str__(self):
        return f"{self.name}"


class LensColor(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False)
    photo_url = models.CharField(max_length=255, null=False)

    lens = models.ForeignKey(Lens, on_delete=models.CASCADE, null=False, related_name="lens_color")

    def __str__(self):
        return f"{self.name}"


class Material(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False)

    frame = models.ForeignKey(Frame, on_delete=models.CASCADE, null=False, related_name="frame_material")

    def __str__(self):
        return f"{self.name}"


class MaterialColor(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False)
    photo_url = models.CharField(max_length=255, null=False)

    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=False, related_name="material_color")
    
    def __str__(self):
        return f"{self.name}"
