import model
from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
import stripe
stripe.api_key = 'sk_test_51Ii3VSHZSFO5KMsTXXB16RAYpJldhvB62V2NNOYOXUuwM0XUvOmXfS7UsKKFKqaezrnDgZYqomvhJaBdLRLCA0q600zyhqTspA'
app = Flask(__name__)
app.secret_key = 'rehome_session'
app.config.from_pyfile("config.cfg") # Configuration file
db = SQLAlchemy(app) # Connecting to SQLAlchemy
from model.contactUs import *
from model.takeCare import *
from model.rehome import *
from model.login import *
from model.donate import *
from passlib.hash import pbkdf2_sha256 as sha256

def generateHash(password):
  return sha256.hash(password)

def verifyHash(password, hash):
  return sha256.verify(password, hash)

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/validate-user', methods = ['POST'])
def validateUser():
  if(request.method == "POST"):
    emailID = request.form["emailID"]
    password = request.form["password"]
    loginObj = Login.validateUser(emailID) #call validateLogin function from dbConnection file
    if (len(loginObj) > 0):
      for keys, values in enumerate(loginObj):
        if (verifyHash(password, values.password)):
          session["userID"] = values.userID
          session["fullName"] = values.fullName
          session["emailID"] = values.emailID
          session["mobileNumber"] = values.mobileNumber
          return jsonify("Success")
        else:
          return jsonify("Error")
    else:
      return jsonify("Invalid")

@app.route('/logout', methods = ['POST'])
def logout():
  # Destroy session..
  session.pop("userID")
  session.pop("fullName")
  session.pop("emailID")
  session.pop("mobileNumber")
  session.pop("amount")
  return jsonify("Success")

@app.route('/signup')
def signup():
  return render_template("signup.html")

@app.route('/create-user', methods = ['POST'])
def createUser():
  if(request.method == "POST"):
    dbObj = Login(
      fullName=request.form["fullName"],
      emailID=request.form["emailID"],
      mobileNumber=request.form["mobileNumber"],
      password=generateHash(request.form["password"])
    )
    response = dbObj.createUser()
    if (response.userID > 0):
      session["userID"] = response.userID
      session["fullName"] = request.form["fullName"]
      session["emailID"] = request.form["emailID"]
      session["mobileNumber"] = request.form["mobileNumber"]
      return jsonify("Success")
    else:
      return jsonify("Error")

@app.route('/rehome')
def rehome():
  return render_template("rehome.html")

@app.route('/get-rehome')
def getRehome():
  rehomeObj = Rehome.getRehome()
  rehome = []  # Empty list
  for keys, values in enumerate(rehomeObj):
    # print (values.age, values.name)
    rehome.append({
      "RehomeID": values.rehomeID,
      "Age": values.age,
      "Name": values.name,
      "rehomeAddedOn": str(
        values.rehomeAddedOn),  # Convert date to string
    })
  return jsonify({
    "data": rehome,
    "message": "success",
  })

@app.route('/take-care')
def takeCare():
  return render_template("takeCare.html")

@app.route('/save-take-care', methods = ['POST'])
def saveTakeCare():
  if(request.method == "POST"):
    dbObj = TakeCare(
      name = request.form["name"],
      emailID = request.form["emailID"],
      mobileNumber = request.form["mobileNumber"],
      numberOfDays = request.form["numberOfDays"],
      reason = request.form["reason"]
    )
    response = dbObj.createTakeCare()  # Create a new take care
    if (response.takeCareID > 0):
      return jsonify("Success")
    else:
      return jsonify("Error")

@app.route('/donate')
def donate():
  return render_template("donate.html")

@app.route('/contact-us')
def contactUs():
  name = request.args.get('name')
  age = request.args.get('age')
  rehome = request.args.get('rehome')
  if (request.args.get('name') != None):
    message = "Interested in name:" + name + ", age: " + age + ", rehome id: " + rehome  
  else: 
    message = ""
  return render_template("contactUs.html", message=message)

@app.route('/save-contact-us', methods = ['POST'])
def saveContactUs():
  if(request.method == "POST"):
    dbObj = ContactUs(
      name = request.form["name"],
      emailID = request.form["emailID"],
      mobileNumber = request.form["mobileNumber"],
      message = request.form["message"]
    )
    response = dbObj.createContactUs()  # Create a new contact us
    if (response.contactUsID > 0):
      return jsonify("Success")
    else:
      return jsonify("Error")

# YOUR_DOMAIN = 'http://127.0.0.1:5000'
YOUR_DOMAIN = 'http://3.248.224.53'
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
  try:
    checkout_session = stripe.checkout.Session.create(
      payment_method_types=['card'],
      line_items=[
        {
          'price_data': {
            'currency': 'eur',
            'unit_amount': int(request.form["amount"])*100,
            'product_data': {
              'name': 'Donation',
            },
          },
          'quantity': 1,
        },
      ],
      mode='payment',
      success_url=YOUR_DOMAIN + '/thank-you',
      cancel_url=YOUR_DOMAIN + '/cancel',
    )
    session["amount"] = request.form["amount"]
    return jsonify({'id': checkout_session.id})
  except Exception as e:
    return jsonify(error=str(e)), 403

@app.route('/thank-you')
def thankyou():
  dbObj = Donate(
    userID=session["userID"],
    donatedBy=session["fullName"],
    mobileNumber=session["mobileNumber"],
    amount=session["amount"]
  )
  response = dbObj.createDonation()
  return render_template("thankyou.html")

@app.route('/cancel')
def cancelDonation():
  return render_template("cancel.html")

if __name__ == '__main__':
  app.run(debug=True)