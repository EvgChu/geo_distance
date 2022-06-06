

from app.distance import bp
from app import app


@bp.route('/')
def get_distance():

    return "Ok blueprint"