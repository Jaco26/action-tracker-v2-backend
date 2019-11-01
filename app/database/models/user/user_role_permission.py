from app.database.db import db

user_role_permission = db.Table('user_role_permission',
  db.Column('role_id', db.Integer, db.ForeignKey('user_role.id'), primary_key=True),
  db.Column('permission_id', db.Integer, db.ForeignKey('user_permission.id'), primary_key=True)
)