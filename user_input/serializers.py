from rest_framework import serializers
from user_input.models import BloodTestResult, LiverFunctionTestResult, RenalFunctionResult, SampleFile


class SampleFileSerializer(serializers.ModelSerializer):
    # input_file = FileField()

    class Meta:
        model = SampleFile
        fields = ['input_file', 'file_ext', ]



