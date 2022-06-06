from flask import Blueprint

bp = Blueprint('distance', __name__)

from app.distance import routes
