from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from user_input.models import BloodTestInfo
from django.http import HttpResponse


class DashboardView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }

        return render(self.request, 'dash/index.html', context)


class FileImportView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {

        }

        return render(self.request, 'dash/file_import.html', context)

    def post(self, request, *args, **kwargs):
        has_content = False
        upload_file = request.FILES.get('upload_file')
        if upload_file:
            file_str = str(upload_file)
            if file_str.endswith('.csv') or file_str.endswith('.png'):
                # do csv or png file manipulation here
                blood_test_qs = BloodTestInfo.objects.filter(user=request.user)
                if blood_test_qs.exists():
                    blood_test_obj = blood_test_qs.first()
                    blood_test_obj.blood_test_file = upload_file
                    blood_test_obj.save()
                    messages.success(self.request, 'Your file was received, we will reveiw it shortly')
                    return redirect('dash:upload')
                else:
                    BloodTestInfo.objects.create(user=self.request.user, blood_test_file=upload_file)
                    messages.success(self.request, 'Your file was received, we will reveiw it shortly')
                    return redirect('dash:upload')
            else:
                messages.error(self.request, 'Selected file format is not supported')
                return redirect('dash:upload')
        messages.warning(self.request, 'Please upload a valid PNG or CSV file')
        return redirect('dash:upload')
