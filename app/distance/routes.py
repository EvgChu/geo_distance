
from flask import request, jsonify
from app.distance import bp
from config import Config
from .geoService import (YaGeoService,
                        UnexpectedResponse,
                        NothingFound,
                        InvalidKey
)
from .distance import DistanceFromMKAD
import logging


LOG = logging.getLogger(__name__)
geo = YaGeoService(Config.YANDEX_API_KEY)
metr = DistanceFromMKAD()

@bp.route('/')
def get_distance():
    if "address" in request.args:
        try:
            points = geo.coordinates(request.args["address"])
        except (UnexpectedResponse, NothingFound):
            LOG.warning('Not correct request:')
            return jsonify({'error': "Not correct request"}), 400
        except InvalidKey:
            LOG.critical('Server error')
            return jsonify({'error': "Server error"}), 500
        LOG.info('Get coordinate for ' + request.args["address"])
        distance_km = metr.distance(points)
        return jsonify({
            "distance": distance_km,
            "address": request.args["address"]
            })
    LOG.warning('Empty request')
    return jsonify({'error': "Empty request"})