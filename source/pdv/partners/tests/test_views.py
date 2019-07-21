import pytest
from rest_framework import status

from pdv.partners.models import Partner


@pytest.mark.django_db
class TestPartner:

    @pytest.fixture
    def partner_payload(self):
        return {
            "id": 1,
            "trading_name": "Adega da Cerveja - Pinheiros",
            "owner_name": "Zé da Silva",
            "document": "1432132123891/0001",
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

    def test_201_created_should_create_a_partner_with_success(
        self,
        client,
        partner_payload
    ):
        response = client.post(
            '/partners/',
            data=partner_payload,
            format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED

        partner = Partner.objects.first()
        assert partner.coverage_area
        assert partner.address

    def test_400_bad_request_should_invalid_address(
        self,
        client,
        partner_payload
    ):
        partner_payload['address']['coordinates'] = []
        response = client.post(
            '/partners/',
            data=partner_payload,
            format='json'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_400_bad_request_should_invalid_coverage_area(
        self,
        client,
        partner_payload
    ):
        partner_payload['coverage_area']['coordinates'] = [[[[
            -43.36556,
            -22.99669
        ]]]]

        response = client.post(
            '/partners/',
            data=partner_payload,
            format='json'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_400_bad_request_should_unique_document(
        self,
        client,
        partner_payload
    ):
        client.post(
            '/partners/',
            data=partner_payload,
            format='json'
        )

        response = client.post(
            '/partners/',
            data=partner_payload,
            format='json'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()['document'] == (
            ['partner with this document already exists.']
        )

    def test_200_ok_should_retrieve_partner(self, client, partner_payload):
        response = client.post(
            '/partners/',
            data=partner_payload,
            format='json'
        )

        partner_id = response.json()['id']

        response = client.get(
            f'/partners/{partner_id}/',
            data=partner_payload,
            format='json'
        )

        assert response.status_code == status.HTTP_200_OK

    def test_204_not_content_should_delete_partner(
        self,
        client,
        partner_payload
    ):
        response = client.post(
            '/partners/',
            data=partner_payload,
            format='json'
        )

        partner_id = response.json()['id']

        response = client.delete(
            f'/partners/{partner_id}/',
            data=partner_payload,
            format='json'
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_200_ok_should_patch_partner(
        self,
        client,
        partner_payload
    ):
        response = client.post(
            '/partners/',
            data=partner_payload,
            format='json'
        )

        partner_id = response.json()['id']

        response = client.patch(
            f'/partners/{partner_id}/',
            data={'document': '1432132123891/0003'},
            format='json'
        )

        assert response.status_code == status.HTTP_200_OK

    def test_200_ok_should_list_partner(
        self,
        client,
        partner_payload
    ):
        response = client.post(
            '/partners/',
            data=partner_payload,
            format='json'
        )

        response = client.get(
            f'/partners/',
            format='json'
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.json()['features']
        assert response.json()['next'] is None

    def test_200_ok_should_filter_partner(
        self,
        client,
        partner_payload
    ):
        client.post(
            '/partners/',
            format='json'
        )
        response = client.get(
            f'/partners/?dist=4000&point=-122.4862,37.7694',
            format='json'
        )
        assert response.status_code == status.HTTP_200_OK
