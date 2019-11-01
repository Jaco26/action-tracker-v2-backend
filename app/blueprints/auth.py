from datetime import timedelta
from flask import Blueprint, jsonify, make_response, request, abort
from passlib.hash import pbkdf2_sha256
from app.database.models import RegisteredUser, UserProfile
from app.util.validate import should_look_like
from app.util.jwt_manager import create_access_token, decode_token


auth_bp = Blueprint('auth_bp', __name__)

def make_token(identity, expires_hours, user_profile):
  return create_access_token(identity, 
                            expires_delta=timedelta(expires_hours),
                            user_claims={
                              'permission': user_profile.role.permission,
                            })


@auth_bp.route('/user-session')
def user_session():
  id_token = request.cookies.get('id_token')
  if id_token:
    return jsonify(id_token)
  abort(403)



@auth_bp.route('/register', methods=['POST'])
def register():
  body = should_look_like({
    'username': str,
    'password': str,
  })


  if not RegisteredUser.find_by_username(body['username']):

    pw_hash = pbkdf2_sha256.hash(body['password'])

    new_user = RegisteredUser(username=body['username'], pw_hash=pw_hash)

    new_user.save_to_db()

    user_profile = UserProfile(user_id=new_user.id, username=new_user.username, role_id=1)

    user_profile.save_to_db()

    id_token = make_token(new_user.id, 1, user_profile)

    res = make_response()

    res.set_cookie('id_token', id_token, httponly=True)

    return res, 201
  
  return 'Username: "{}" has already been taken'.format(body['username']), 403



@auth_bp.route('/login', methods=['POST'])
def login():
  body = should_look_like({
    'username': str,
    'password': str,
  })

  user = RegisteredUser.find_by_username(body['username'])

  if user and pbkdf2_sha256.verify(body['password'], user.pw_hash):

    user_profile = UserProfile.query.get(user.id)

    id_token = make_token(user.id, 1, user_profile)

    res = make_response()

    res.set_cookie('id_token', id_token, httponly=True)

    return res, 201

  abort(403)
