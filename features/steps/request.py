import functools
import json

import random
import requests
from behave import step


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


@step('Create a partner with document')
def create_a_partner(context):
    payload = {
        "id": 1,
        "trading_name": "Adega da Cerveja - Pinheiros",
        "owner_name": "Zé da Silva",
        "document": "1432132123891/000{}".format(random.randint(100, 500)),
        "coverage_area": {
            "type": "MultiPolygon",
            "coordinates": [[[[
                -43.36556,
                -22.99669
            ], [
                -43.36539,
                -23.01928
            ], [
                -43.26583,
                -23.01802
            ], [
                -43.25724,
                -23.00649
            ], [
                -43.23355,
                -23.00127
            ], [
                -43.2381,
                -22.99716
            ], [
                -43.23866,
                -22.99649
            ], [
                -43.24063,
                -22.99756
            ], [
                -43.24634,
                -22.99736
            ], [
                -43.24677,
                -22.99606
            ], [
                -43.24067,
                -22.99381
            ], [
                -43.24886,
                -22.99121
            ], [
                -43.25617,
                -22.99456
            ], [
                -43.25625,
                -22.99203
            ], [
                -43.25346,
                -22.99065
            ], [
                -43.29599,
                -22.98283
            ], [
                -43.3262,
                -22.96481
            ], [
                -43.33427,
                -22.96402
            ], [
                -43.33616,
                -22.96829
            ], [
                -43.342,
                -22.98157
            ], [
                -43.34817,
                -22.97967
            ], [
                -43.35142,
                -22.98062
            ], [
                -43.3573,
                -22.98084
            ], [
                -43.36522,
                -22.98032
            ], [
                -43.36696,
                -22.98422
            ], [
                -43.36717,
                -22.98855
            ], [
                -43.36636,
                -22.99351
            ], [
                -43.36556,
                -22.99669
            ]]]]
        },
        "address": {
            "type": "Point",
            "coordinates": [-43.297337, -23.013538]
        },
    }
    context.response = post(
        access_token=context.access_token,
        base_url=context.settings['base_url'],
        endpoint='/partners/',
        data=payload
    )


@step('Update a partner with document')
def update_a_partner(context):
    payload = {
        "id": context.response.json()['id'],
        "trading_name": "Adega da Cerveja - Pinheiros",
        "owner_name": "Zé da Silva",
        "document": "1432132123891/000{}".format(random.randint(100, 500)),
        "coverage_area": {
            "type": "MultiPolygon",
            "coordinates": [[[[
                -43.36556,
                -22.99669
            ], [
                -43.36539,
                -23.01928
            ], [
                -43.26583,
                -23.01802
            ], [
                -43.25724,
                -23.00649
            ], [
                -43.23355,
                -23.00127
            ], [
                -43.2381,
                -22.99716
            ], [
                -43.23866,
                -22.99649
            ], [
                -43.24063,
                -22.99756
            ], [
                -43.24634,
                -22.99736
            ], [
                -43.24677,
                -22.99606
            ], [
                -43.24067,
                -22.99381
            ], [
                -43.24886,
                -22.99121
            ], [
                -43.25617,
                -22.99456
            ], [
                -43.25625,
                -22.99203
            ], [
                -43.25346,
                -22.99065
            ], [
                -43.29599,
                -22.98283
            ], [
                -43.3262,
                -22.96481
            ], [
                -43.33427,
                -22.96402
            ], [
                -43.33616,
                -22.96829
            ], [
                -43.342,
                -22.98157
            ], [
                -43.34817,
                -22.97967
            ], [
                -43.35142,
                -22.98062
            ], [
                -43.3573,
                -22.98084
            ], [
                -43.36522,
                -22.98032
            ], [
                -43.36696,
                -22.98422
            ], [
                -43.36717,
                -22.98855
            ], [
                -43.36636,
                -22.99351
            ], [
                -43.36556,
                -22.99669
            ]]]]
        },
        "address": {
            "type": "Point",
            "coordinates": [-43.297337, -23.013538]
        },
    }

    context.response = put(
        access_token=context.access_token,
        base_url=context.settings['base_url'],
        endpoint='/partners/{}/'.format(context.response.json()['id']),
        data=payload
    )


@step('Delete a partner with id')
def delete_a_partner(context):
    context.response = delete(
        access_token=context.access_token,
        base_url=context.settings['base_url'],
        endpoint='/partners/{}'.format(context.response.json()['id']),
    )


@step('Find a partner with id "{partner_id}"')
def get_a_partner(context, partner_id):
    context.response = get(
        access_token=context.access_token,
        base_url=context.settings['base_url'],
        endpoint='/partners/{}'.format(partner_id),
    )


@step('filter a partner')
def filter_a_partner(context):
    context.response = get(
        access_token=context.access_token,
        base_url=context.settings['base_url'],
        endpoint='/partners/?dist=4000&point=-122.4862,37.7694',
    )
