from flask import Flask
import logging
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

logging.basicConfig(filename=Config.LOG_FILE_NAME, level=logging.DEBUG)

from app.distance import bp as distance_bp
app.register_blueprint(distance_bp,  url_prefix='/v1')

