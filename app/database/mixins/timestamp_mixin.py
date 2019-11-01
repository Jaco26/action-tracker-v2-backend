from datetime import datetime
from sqlalchemy.dialects.postgresql import TIMESTAMP
from app.database.db import db

class TimestampMixin:
  date_created = db.Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
  date_updated = db.Column(TIMESTAMP(timezone=True), onupdate=datetime.utcnow)
