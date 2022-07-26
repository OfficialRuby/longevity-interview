from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from user_input.token_auth import TokenAuthentication
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View
from user_input.models import BloodTestInfoFile, BloodTestInfo
from django.http import HttpResponse
from user_input.serializers import BloodGroupSerializers
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.core.exceptions import FieldDoesNotExist


class FileImportView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        token = Token.objects.filter(user=request.user).first()
        context = {
            'token': token,

        }

        return render(self.request, 'dash/file_import.html', context)

    def post(self, request, *args, **kwargs):
        has_content = False
        upload_file = request.FILES.get('upload_file')
        if upload_file:
            file_str = str(upload_file)
            if file_str.endswith('.csv'):
                # do csv or png file manipulation here
                blood_test_qs = BloodTestInfoFile.objects.filter(user=request.user)
                if blood_test_qs.exists():
                    blood_test_obj = blood_test_qs.first()
                    blood_test_obj.blood_test_file = upload_file
                    blood_test_obj.file_ext = 'csv'
                    blood_test_obj.save()
                    messages.success(self.request, 'Your file was received, we will reveiw it shortly')
                    return redirect('dash:upload')
                else:
                    BloodTestInfoFile.objects.create(
                        user=self.request.user, blood_test_file=upload_file, file_ext='png')
                    messages.success(self.request, 'Your file was received, we will reveiw it shortly')
                    return redirect('dash:upload')
            else:
                messages.error(self.request, 'Selected file format is not supported')
                return redirect('dash:upload')
        messages.warning(self.request, 'Please upload a valid PNG or CSV file')
        return redirect('dash:upload')


class GadgetDataEntry(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serialize = BloodGroupSerializers(data=request.data)
        bearer = request.headers.get('Authorization')
        bearer_token = bearer.split(' ')[-1]
        user_token = Token.objects.get(key=bearer_token)
        user = user_token.user

        if serialize.is_valid():
            try:
                blood_test = BloodTestInfo.objects.filter(user=user)
                if blood_test.exists():
                    blood_test.update(
                        **request.data
                    )
                    return Response({'status': status.HTTP_201_CREATED,
                                    'message': 'Blood test data updated successfully'})

                else:
                    BloodTestInfo.objects.create(
                        user=user,
                        **request.data,
                    )

                    return Response({'status': status.HTTP_200_OK,
                                    'message': 'Blood test data created successfully'})
            except FieldDoesNotExist as e:
                return Response({'status': status.HTTP_406_NOT_ACCEPTABLE,
                                 'message': 'Invalid parameter supplied'})

        return Response(serialize.errors)
