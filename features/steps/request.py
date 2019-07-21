import functools
import json

import requests


def request(method, base_url, endpoint, access_token, data=None):
    body = json.dumps(data) if data else None

    return requests.request(
        method,
        '{base_url}{endpoint}'.format(base_url=base_url, endpoint=endpoint),
        headers={
            'Authorization': 'Bearer {}'.format(access_token),
            'Content-Type': 'application/json',
        },
        data=body
    )


get = functools.partial(request, 'GET')
post = functools.partial(request, 'POST')
patch = functools.partial(request, 'PATCH')
delete = functools.partial(request, 'DELETE')
put = functools.partial(request, 'PUT')
options = functools.partial(request, 'OPTIONS')
