from django.db import models
from django.contrib.auth.models import User


class BloodTestInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blod_pressure = models.CharField(max_length=100, blank=True, null=True)
    blod_type = models.CharField(max_length=100, blank=True, null=True)
    blod_rhd = models.CharField(max_length=100, blank=True, null=True)
    blood_test_file = models.FileField(upload_to='blood_test_files')

    def __str__(self):
        return self.user.username
