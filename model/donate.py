from app import db
import datetime

class Donate(db.Model):
  __tablename__ = "donate" # Defining table name

  donateID = db.Column(db.Integer, primary_key=True, autoincrement=True)
  userID = db.Column(db.Integer)
  donatedBy = db.Column(db.String(100))
  mobileNumber = db.Column(db.String(15))
  amount = db.Column(db.Float)
  donatedOn = db.Column(db.DateTime, default=datetime.datetime.utcnow)

  def createDonation(self):
    db.session.add(self)
    db.session.commit()
    db.session.flush()
    return self