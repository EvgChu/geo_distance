import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    YANDEX_API_KEY = "5c7fa568-dad0-48ed-8a75-c87b879b869b"
