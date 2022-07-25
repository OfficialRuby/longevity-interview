from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from user_input.views import FileImportView, GadgetDataEntry

app_name = 'dash'
urlpatterns = [
    path('', FileImportView.as_view(), name='upload'),
    path('entry-gadget/', GadgetDataEntry.as_view(), name='gadget_entry'),

]
