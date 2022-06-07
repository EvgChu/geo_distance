
from flask import request, jsonify
from app.distance import bp
from config import Config
from .geoService import (YaGeoService,
                        UnexpectedResponse,
                        NothingFound,
                        InvalidKey
)

import logging
LOG = logging.getLogger(__name__)

geo = YaGeoService(Config.YANDEX_API_KEY)

@bp.route('/')
def get_distance():
    if "address" in request.args:
        try:
            points = geo.coordinates(request.args["address"])
        except (UnexpectedResponse, NothingFound):
            LOG.warning('Not correct request:')
            return jsonify({'error': "Not correct request"})
        except InvalidKey:
            LOG.critical('Server error')
            return jsonify({'error': "Server error"})
        LOG.info('Get coordinate for ' + request.args["address"])

        return jsonify({
            "distance": points,
            "address": request.args["address"]
            })
    return "Ok blueprint"