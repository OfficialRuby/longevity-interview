from django.contrib import admin
from user_input.models import BloodTestResult, LiverFunctionTestResult, RenalFunctionResult
admin.site.register(BloodTestResult)
admin.site.register(LiverFunctionTestResult)
admin.site.register(RenalFunctionResult)
