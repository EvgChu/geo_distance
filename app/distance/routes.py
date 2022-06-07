
from flask import request, jsonify
from app.distance import bp
from config import Config
from .geoService import YaGeoService

geo = YaGeoService(Config.YANDEX_API_KEY)

@bp.route('/')
def get_distance():
    if "address" in request.args:
        points = geo.coordinates(request.args["address"])
        return jsonify({"distance": points})
    return "Ok blueprint"