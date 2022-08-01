from django.urls import path
from tracker_entry.views import GoogleFitImportView, get_user_token_view

urlpatterns = [
    path('entry/google-fit/', GoogleFitImportView.as_view(), name='google_fit_connect'),
    path('entry/google-fit/response/', get_user_token_view, name='google_fit_response'),

]
