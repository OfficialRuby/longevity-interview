import google_auth_oauthlib.flow


def google_fit_auth():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/fitness.activity.read'])

    flow.redirect_uri = 'http://localhost:8000/app/connection-response/'

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')
    return authorization_url
