from rest_framework import serializers
from user_input.models import BloodTestInfo


class BloodGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = BloodTestInfo
        fields = ['blood_pressure', 'blood_type', 'blood_rhd', ]
