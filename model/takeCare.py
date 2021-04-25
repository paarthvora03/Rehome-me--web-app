from app import db
import datetime

class TakeCare(db.Model):
  __tablename__ = "takeCare" # Defining table name

  takeCareID = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(100))
  emailID = db.Column(db.String(100))
  mobileNumber = db.Column(db.String(15))
  numberOfDays = db.Column(db.Integer)
  reason = db.Column(db.Text)
  takeCareAddedOn = db.Column(db.DateTime, default=datetime.datetime.utcnow)

  @classmethod
  def getTakeCare():
    return TakeCare.query.all()

  def createTakeCare(self):
    db.session.add(self)
    db.session.commit()
    db.session.flush()
    return self