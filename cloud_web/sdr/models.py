from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Sdr(models.Model):
    ip = models.GenericIPAddressField()
    name = models.CharField(max_length=20)
    loc_x = models.FloatField(max_length=10)
    loc_y = models.FloatField(max_length=10)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    p_id = models.IntegerField(max_length=6)
    def __str__(self):
        return self.name