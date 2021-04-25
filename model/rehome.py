from app import db
import datetime

class Rehome(db.Model):
  __tablename__ = "rehome" # Defining table name

  rehomeID = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(50))
  age = db.Column(db.String(15))
  rehomeAddedOn = db.Column(db.DateTime, default=datetime.datetime.utcnow)

  @classmethod
  def getRehome(self):
    return Rehome.query.all()