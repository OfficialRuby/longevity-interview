from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class SampleFile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    input_file = models.FileField(upload_to='test_files', blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=['csv', ])
    ])
    file_ext = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class BloodTestResult(models.Model):
    class Meta:
        verbose_name_plural = 'Blood Test Results'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hemoglobin = models.CharField("Hemoglobin", max_length=50, blank=True, null=True)
    white_cell_count = models.CharField("White Cell Count", max_length=50, blank=True, null=True)
    sodium = models.CharField("Sodium", max_length=50, blank=True, null=True)
    potassium = models.CharField("Potassium", max_length=50, blank=True, null=True)
    urea = models.CharField("Urea", max_length=50, blank=True, null=True)
    platelet_count = models.CharField("Platelet", max_length=50, blank=True, null=True)
    amylase = models.CharField("Amylase", max_length=50, blank=True, null=True)
    test_file = models.ForeignKey(SampleFile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class LiverFunctionTestResult(models.Model):
    class Meta:
        verbose_name_plural = 'Liver Function Test Results'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    albumin = models.CharField('Albumin', max_length=50, blank=True, null=True)
    total_bilirubin = models.CharField('Total Bilirubin', max_length=50, blank=True, null=True)
    conjugate_bilirubin = models.CharField('Conjugate Bilirubin', max_length=50, blank=True, null=True)
    alanine_aminotransferase = models.CharField('alanine Aminotransferase', max_length=50, blank=True, null=True)
    alkaline_phosphate = models.CharField('Alkaline Phosphate', max_length=50, blank=True, null=True)
    test_file = models.ForeignKey(SampleFile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class RenalFunctionResult(models.Model):
    class Meta:
        verbose_name_plural = "Renal Function Results"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    urea = models.CharField('Urea', max_length=50, blank=True, null=True)
    creatinine = models.CharField('Creatnine', max_length=50, blank=True, null=True)
    sodium = models.CharField('Sodium', max_length=50, blank=True, null=True)
    potassium = models.CharField('Potassium', max_length=50, blank=True, null=True)
    chloride = models.CharField('Chloride', max_length=50, blank=True, null=True)
    test_file = models.ForeignKey(SampleFile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
