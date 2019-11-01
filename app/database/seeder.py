from app.database.db import db
from app.database.models import UserRole, UserPermission

def seed_db():
  role_user = UserRole(name='user')
  role_admin = UserRole(name='admin')

  db.session.add_all([
    role_user,
    role_admin,
  ])
 
  perm_user = UserPermission(name='user')
  perm_admin = UserPermission(name='admin')

  role_user.permission.append(perm_user)

  role_admin.permission.append(perm_user)
  role_admin.permission.append(perm_admin)

  db.session.add_all([
    perm_user,
    perm_admin
  ])

  db.session.commit()