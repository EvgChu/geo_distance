from flask import Flask
import logging
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.distance import bp as distance_bp
app.register_blueprint(distance_bp)

