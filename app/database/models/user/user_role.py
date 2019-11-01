from app.database.db import db

class UserRole(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  permission = db.relationship('UserPermission', secondary='user_role_permission', lazy='joined')

  def __repr__(self):
    return f"UserRole {self.id} - {self.name} - {self.permission}"

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()