
from flask import request, jsonify
from app.distance import bp
from config import Config
from .geoService import (YaGeoService,
                        UnexpectedResponse,
                        NothingFound,
                        InvalidKey
)

geo = YaGeoService(Config.YANDEX_API_KEY)

@bp.route('/')
def get_distance():
    if "address" in request.args:
        try:
            points = geo.coordinates(request.args["address"])
        except (UnexpectedResponse, NothingFound):
            return jsonify({"Not correct request": points})
        except InvalidKey:
            return jsonify({"Server error": points})
        return jsonify({
            "distance": points,
            "address": request.args["address"]
            })
    return "Ok blueprint"