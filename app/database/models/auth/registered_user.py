from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.database.db import db
from app.database.mixins import TimestampMixin

class RegisteredUser(TimestampMixin, db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
  username = db.Column(db.String, nullable=False, unique=True)
  pw_hash = db.Column(db.String, nullable=False)

  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(username=username).first()

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()