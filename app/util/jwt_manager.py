import functools
from flask import abort
from flask_jwt_extended import *
from app.database.models import RevokedToken

jwt = JWTManager()

@jwt.token_in_blacklist_loader
def is_token_revoked(decrypted_token):
  jti = decrypted_token.get('jti')
  return RevokedToken.is_token_revoked(jti)


# custom decorators

def with_permission(permission):
  def idk(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      verify_jwt_in_request()
      claims = get_jwt_claims()
      user_permission = claims.get('permission')
      if permission not in user_permission:
        abort(403)
      return func(*args, **kwargs)
    return wrapper
  return idk
