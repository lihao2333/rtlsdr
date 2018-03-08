from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from sdr.models import Sdr
# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}/{2}'.format(instance.owner.username, instance.time, filename)
class Data(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name="data_owner")
    loc_x = models.FloatField()
    loc_y = models.FloatField()
    fs = models.FloatField()
    dt = models.FloatField()
    fc = models.FloatField()
    gain = models.FloatField()
    data = models.FileField(upload_to=user_directory_path)
    time = models.DateTimeField(default=timezone.now())
