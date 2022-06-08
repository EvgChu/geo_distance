
import geojson 
from geopy.distance import geodesic
from typing import Tuple
from decimal import Decimal
from shapely.geometry import Point, Polygon
from shapely.ops import nearest_points
from .coordinates import Coordinates

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
            self.mkad = Polygon(data["coordinates"][0])

    def distance(self, target: Coordinates) -> float:
        """ Представляем МКАД в виде полигона и используя библиотеку shapely
        находи ближашую точку полигона (не вершину) к заданной 
        """
        if self.mkad.contains(Point(target.latitude, target.longitude)):
            return 0
        point = Point(target)
        p1, p2 = nearest_points(self.mkad, point)
        
        return geodesic(target, (p1.x, p1.y)).kilometers

