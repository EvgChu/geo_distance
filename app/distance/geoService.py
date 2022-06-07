from decimal import Decimal
from typing import Tuple

import requests

class ServiceGeocoderException(Exception):
    pass

class UnexpectedResponse(ServiceGeocoderException):
    pass


class NothingFound(ServiceGeocoderException):
    pass


class InvalidKey(ServiceGeocoderException):
    pass


class GeoService:
    """geocoder API client.
    """

    __slots__ = ("api_key",)

    api_key: str

    def __init__(self, api_key: str):
        self.api_key = api_key

    def coordinates(self, address: str) -> Tuple[Decimal]:
        raise NotImplementedError

    def address(self, longitude: Decimal, latitude: Decimal) -> str:
        raise NotImplementedError


class YaGeoService(GeoService):
    """Yandex API client.
    """
    URL_YANDEX_API = "https://geocode-maps.yandex.ru/1.x/"
    __slots__ = ()

    def _request(self, address: str) -> dict:
        response = requests.get(
            YaGeoService.URL_YANDEX_API,
            params=dict(format="json", apikey=self.api_key, geocode=address),
        )

        if response.status_code == 200:
            return response.json()["response"]
        elif response.status_code == 403:
            raise InvalidKey()
        else:
            raise UnexpectedResponse(
                f"status_code={response.status_code}, body={response.content}"
            )

    def coordinates(self, address: str) -> Tuple[Decimal]:
        """Fetch coordinates (longitude, latitude) for passed address."""
        data = self._request(address)["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{address}" not found')

        coordinates = data[0]["GeoObject"]["Point"]["pos"]  # type: str
        longitude, latitude = tuple(coordinates.split(" "))

        return Decimal(latitude), Decimal(longitude)

    def address(self, longitude: Decimal, latitude: Decimal) -> str:
        """Fetch address for passed coordinates."""
        got = self._request(f"{longitude},{latitude}")
        data = got["GeoObjectCollection"]["featureMember"]

        if not data:
            raise NothingFound(f'Nothing found for "{longitude} {latitude}"')

        return data[0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]
