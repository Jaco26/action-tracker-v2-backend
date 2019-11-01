from app.database.db import db

class UserPermission(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)

  def __repr__(self):
    return f"UserPermission {self.id} - {self.name}"

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()