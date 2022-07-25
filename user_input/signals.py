from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from user_input.models import BloodTestInfo, BloodTestInfoFile
import pandas as pd
import os
from django.conf import settings
from django.contrib.auth.models import User


def serialize_csv_data(sender, instance, **kwargs):
    if instance.file_ext == 'csv':
        instance_path = str(instance.blood_test_file.url)
        base_path = instance_path[1:]
        csv_df = pd.read_csv(os.path.join(settings.BASE_DIR, base_path), )
        csv_df.columns = csv_df.columns.str.strip()
        blood_pressure = csv_df['blood_pressure'].values[0]
        blood_rhd = csv_df['blood_rhd'].values[0]
        blood_type = csv_df['blood_type'].values[0]
        blood_test = BloodTestInfo.objects.filter(user=instance.user)
        if blood_test:
            blood_test.update(
                blood_pressure=blood_pressure,
                blood_type=blood_type,
                blood_rhd=blood_rhd,
                sample_file=instance,
            )
        else:
            BloodTestInfo.objects.create(
                blood_pressure=blood_pressure,
                blood_type=blood_type,
                blood_rhd=blood_rhd,
                sample_file=instance,
            )


@receiver(post_save, sender=User)
def generate_auth_token(sender, instance, created, ** kwargs):
    if created:
        Token.objects.create(user=instance)


post_save.connect(serialize_csv_data, sender=BloodTestInfoFile)
