from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from user_input.models import BloodTestResult, LiverFunctionTestResult, RenalFunctionResult, SampleFile
import pandas as pd
import os
from django.conf import settings
from django.contrib.auth.models import User


def serialize_csv_data(sender, instance, **kwargs):
    if instance.file_ext == 'csv':
        instance_path = str(instance.input_file.url)
        base_path = instance_path[1:]
        csv_df = pd.read_csv(os.path.join(settings.BASE_DIR, base_path), )
        csv_df.columns = csv_df.columns.str.strip()
        hemoglobin = csv_df['hemoglobin'].values[0]
        white_cell_count = csv_df['white_cell_count'].values[0]
        sodium = csv_df['sodium'].values[0]
        potassium = csv_df['potassium'].values[0]
        urea = csv_df['urea'].values[0]
        platelet_count = csv_df['platelet_count'].values[0]
        amylase = csv_df['amylase'].values[0]
        albumin = csv_df['albumin'].values[0]
        total_bilirubin = csv_df['total_bilirubin'].values[0]
        conjugate_bilirubin = csv_df['conjugate_bilirubin'].values[0]
        alanine_aminotransferase = csv_df['alanine_aminotransferase'].values[0]
        alkaline_phosphate = csv_df['alkaline_phosphate'].values[0]
        urea = csv_df['urea'].values[0]
        creatinine = csv_df['creatinine'].values[0]
        sodium = csv_df['sodium'].values[0]
        potassium = csv_df['potassium'].values[0]
        chloride = csv_df['chloride'].values[0]
        blood_test_result = BloodTestResult.objects.filter(user=instance.user)
        liver_func_test = LiverFunctionTestResult.objects.filter(user=instance.user)
        renal_func_test = RenalFunctionResult.objects.filter(user=instance.user)
        if blood_test_result:
            blood_test_result.update(
                hemoglobin=hemoglobin,
                white_cell_count=white_cell_count,
                sodium=sodium,
                potassium=potassium,
                urea=urea,
                platelet_count=platelet_count,
                amylase=amylase,
                test_file=instance,
            )
        else:
            BloodTestResult.objects.create(
                user=instance.user,
                hemoglobin=hemoglobin,
                white_cell_count=white_cell_count,
                sodium=sodium,
                potassium=potassium,
                urea=urea,
                platelet_count=platelet_count,
                amylase=amylase,
                test_file=instance,)
        if liver_func_test:
            liver_func_test.update(
                albumin=albumin,
                total_bilirubin=total_bilirubin,
                conjugate_bilirubin=conjugate_bilirubin,
                alanine_aminotransferase=alanine_aminotransferase,
                alkaline_phosphate=alkaline_phosphate,
                test_file=instance,
            )
        else:
            LiverFunctionTestResult.objects.create(
                user=instance.user,
                albumin=albumin,
                total_bilirubin=total_bilirubin,
                conjugate_bilirubin=conjugate_bilirubin,
                alanine_aminotransferase=alanine_aminotransferase,
                alkaline_phosphate=alkaline_phosphate,
                test_file=instance,
            )
        if renal_func_test:
            renal_func_test.update(
                urea=urea,
                creatinine=creatinine,
                sodium=sodium,
                potassium=potassium,
                chloride=chloride,
                test_file=instance,
            )
        else:
            RenalFunctionResult.objects.create(
                user=instance.user,
                urea=urea,
                creatinine=creatinine,
                sodium=sodium,
                potassium=potassium,
                chloride=chloride,
                test_file=instance,
            )


@ receiver(post_save, sender=User)
def generate_auth_token(sender, instance, created, ** kwargs):
    if created:
        Token.objects.create(user=instance)


post_save.connect(serialize_csv_data, sender=SampleFile)
