from flask.json import JSONEncoder
from datetime import date, tzinfo, timedelta
from uuid import UUID
from app.database.db import db

class SimpleUTC(tzinfo):
  def tzname(self, **kwargs):
    return 'UTC'

  def utcoffset(self, dt):
    return timedelta(0)


class ExtendedJSONEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, date):
      return obj.replace(tzinfo=SimpleUTC()).isoformat()
    elif isinstance(obj, timedelta):
      return str(obj)
    elif isinstance(obj, UUID):
      return str(obj)
    elif isinstance(obj, db.Model):
      return obj.cols_dict()
    return JSONEncoder.default(obj)