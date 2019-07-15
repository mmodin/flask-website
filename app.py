from flask import Flask, flash, redirect, render_template, request, session, abort
from models import User
from shared_models import db
from password import hash_plaintext_pw
from database import db_validate_user_pw, db_register_new_user
from config import DB_CONNECT_STRING


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_CONNECT_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
	db.create_all()
	

@app.route("/")
def home():
	if not session.get("logged_in"):
		return render_template("login.html")
	else:
		return 'Hello Boss!  <a href="/logout">Logout</a>'


@app.route("/signup", methods=["GET", "POST"])
def signup():
	error = None
	if request.method == "POST":
		post_username = str(request.form["username"])
		post_password = str(request.form["password"])
		post_email = str(request.form["email"])
		post_password_repeat = str(request.form["password_repeat"])
		if post_password == post_password_repeat:
			db_register_new_user(post_username, post_password, post_email)
			session["logged_in"] = True
			return home()
		else:
			flash("bblbllblblb")
	return render_template("signup.html")
		
		
@app.route("/login", methods=["GET", "POST"])
def login():
	error = None
	if request.method == "POST":
		post_username = str(request.form["username"])
		post_password = str(request.form["password"])
		result = db_validate_user_pw(post_username, post_password)
		if result == True:
			session["logged_in"] = True
		else:
			flash("Incorrect username or password!")
		return home()
	return render_template("login.html")
		


@app.route("/logout")
def logout():
	session["logged_in"] = False
	return home()
	
if __name__ == "__main__":
	app.secret_key = "bob"
	app.run(debug=True)