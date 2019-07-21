import requests
from behave import given
from requests.auth import HTTPBasicAuth


def _request_token(context):
    response = requests.post(
        '{}/oauth/token/'.format(context.settings['base_url']),
        auth=HTTPBasicAuth(
            context.settings['client_id'],
            context.settings['client_secret']
        ),
        data={
            'grant_type': 'client_credentials',
            'scope': " ".join(context.settings['scopes'])
        }
    )

    if response.status_code != 200:
        response.raise_for_status()

    access_token = response.json()['access_token']
    context.access_token = access_token


@given(u'My app has an access token')
def request_access_token(context):
    if context.access_token:
        return

    _request_token(context)
