
from app.database.db import db

class RevokedToken(db.Model):
  jti = db.Column(db.String, primary_key=True)

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def is_revoked(cls, jti):
    return bool(cls.query.get(jti))