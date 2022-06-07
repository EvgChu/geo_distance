import os
basedir = os.path.abspath(os.path.dirname(__file__))
from local_config import LocalConfig

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    YANDEX_API_KEY = os.environ.get('YANDEX_API_KEY') or LocalConfig.YANDEX_API_KEY
    LOG_FILE_NAME = ".log"
    