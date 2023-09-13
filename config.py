import os
basedir = os.path.abspath(os.path.dirname(__file__))
try:
    from local_config import LocalConfig
except:
    class LocalConfig:
        YANDEX_API_KEY = os.environ.get('YANDEX_API_KEY') or "bad"
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

class Config(object):
    SECRET_KEY = LocalConfig.SECRET_KEY
    YANDEX_API_KEY = LocalConfig.YANDEX_API_KEY
    LOG_FILE_NAME = ".log"
    