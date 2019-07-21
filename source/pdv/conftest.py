from collections import namedtuple
from datetime import timedelta

import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
from oauth2_provider.models import AccessToken, get_application_model
from rest_framework.test import APIClient

OAuth2Token = namedtuple(
    'oauth2token',
    ['dev_user', 'application', 'access_token']
)


@pytest.fixture
def user():
    return get_user_model().objects.create_user(
        'dev_user', 'dev_user@dev_user.com'
    )


@pytest.fixture
def application():
    application = get_application_model()
    user_application = get_user_model().objects.create_user(
        'dev_user', 'dev@user.com'
    )
    return application.objects.create(
        name='Test',
        user=user_application,
        client_type=application.CLIENT_CONFIDENTIAL,
        authorization_grant_type=application.GRANT_CLIENT_CREDENTIALS,
    )


@pytest.fixture
def client(application):
    access_token = AccessToken.objects.create(
        scope=' '.join(settings.OAUTH2_PROVIDER['SCOPES'].keys()),
        expires=timezone.now() + timedelta(seconds=300),
        token='secret-access-token-key',
        application=application
    )

    oauth2token = OAuth2Token(
        dev_user=application.user,
        application=application,
        access_token=access_token
    )

    client = APIClient()
    client.credentials(
        HTTP_AUTHORIZATION='Bearer {}'.format(oauth2token.access_token.token)
    )

    return client
