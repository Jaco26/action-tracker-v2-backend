from sqlalchemy.dialects.postgresql import UUID
from app.database.db import db
from app.database.mixins import TimestampMixin

class UserProfile(TimestampMixin, db.Model):
  user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('registered_user.id'), primary_key=True)
  role_id = db.Column(db.Integer, db.ForeignKey('user_role.id'))
  username = db.Column(db.String, unique=True, nullable=False)
  role = db.relationship('UserRole', lazy='joined')

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()