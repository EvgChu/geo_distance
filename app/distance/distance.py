
import geojson 
from geopy.distance import geodesic
from typing import Tuple
from decimal import Decimal

class DistanceFromObjects:
    """
        Базовый класс для вычисления расстояний между заданным объектом
        и переданной точкой
    """
    def distance(self, address: str) -> float:
        raise NotImplementedError


class DistanceFromMKAD(DistanceFromObjects):
    """
    """
    FILE_GEOJSON_MKAD = 'app/distance/moscow.json'

    def __init__(self):
        with open(DistanceFromMKAD.FILE_GEOJSON_MKAD) as f:
            data = geojson.loads(f.read())
            self.mkad = data["coordinates"][0]

    def distance(self, target: Tuple[Decimal]) -> float:
        """ Простое вычисления расстояния """
        all_distance = []
        for point in self.mkad:
            all_distance.append(geodesic(point, target).kilometers)
        
        return round(min(all_distance), 3)