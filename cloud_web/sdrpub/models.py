from django.db import models

# Create your models here.
class Sdr(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    name = models.CharField(max_length=20)
    loc_x = models.FloatField(max_length=10)
    loc_y = models.FloatField(max_length=10)
    state = models.BooleanField(default=True)
    def __str__(self):
        return self.name
