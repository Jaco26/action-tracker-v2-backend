import os

class BaseConfig:
  ENABLE_CORS = True

  JWT_BLACKLIST_ENABLED = True
  JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
  JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  SQLALCHEMY_TRACK_MODIFICATIONS = False