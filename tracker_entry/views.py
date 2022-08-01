from django.http import HttpResponseBadRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import googleapiclient.discovery
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
import google_auth_oauthlib.flow

CLIENT_SECTRET = 'fitness_app_client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/fitness.activity.read',
          'https://www.googleapis.com/auth/fitness.blood_glucose.read',
          'https://www.googleapis.com/auth/fitness.blood_pressure.read',
          'https://www.googleapis.com/auth/fitness.body.read',
          'https://www.googleapis.com/auth/fitness.body_temperature.read']
REDIRECT_URI = 'http://localhost:8000/entry/google-fit/response/'

'''
I have decided to make all code available in one file in order to make review easier
This code splitted or grouped into chunks of code and then connected to form a working system
'''


class GoogleFitImportView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            CLIENT_SECTRET,
            scopes=SCOPES)

        flow.redirect_uri = REDIRECT_URI

        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true')
        return redirect(authorization_url)


@login_required
def get_user_token_view(request):
    if request.method == 'GET':
        if not 'error' in request.GET:
            try:
                state = request.GET.get('state')
                flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
                    CLIENT_SECTRET,
                    scopes=SCOPES,
                    state=state)
                flow.redirect_uri = REDIRECT_URI

                authorization_response = request.build_absolute_uri()

                flow.fetch_token(authorization_response=authorization_response)
                credentials = flow.credentials
                service = build('fitness', 'v1', credentials=creds)

                response = fit.users().dataSources().list(userId='me').execute()
                messages.success(request, 'Your health data was imported successfully')
                return redirect('dash:upload')
            except Exception as e:
                # The major error that could occur here is making request over HTTP
                # As authentication credentials is only available via HTTPS
                # Solution for testing this execise can be done by making the request via a secured connection
                messages.error(request, f'Error occured: {e} ')
                return redirect('dash:upload')
        messages.warning(request, 'A problem was encountered, please try again')
        return redirect('dash:upload')
    return HttpResponseBadRequest('Method not implemented')
