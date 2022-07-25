from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class BloodTestInfoFile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_test_file = models.FileField(upload_to='blood_test_files', blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=['csv', ])
    ])
    file_ext = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class BloodTestInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_pressure = models.CharField(max_length=100, blank=True, null=True)
    blood_type = models.CharField(max_length=100, blank=True, null=True)
    blood_rhd = models.CharField(max_length=100, blank=True, null=True)
    m_unit = models.CharField(max_length=50, blank=True, null=True)
    sample_file = models.ForeignKey(BloodTestInfoFile, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
