from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user_input.views import DashboardView, FileImportView

app_name = 'dash'
urlpatterns = [
    path('', DashboardView.as_view(), name='dash'),
    path('upload/', FileImportView.as_view(), name='upload'),

]
