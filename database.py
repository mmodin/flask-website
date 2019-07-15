from shared_models import db
from models import User
from config import DB_CONNECT_STRING


def db_validate_user_pw(username, password):
	user = User.query.filter_by(username=username).first()
	if user:
		validation_result = user.check_password(password)
		return validation_result
	else:
		print("No user named '{}' found!".format(username))
		return False

		
def db_register_new_user(username, password, email):
	new_user = User(username, email=email)
	new_user.set_password(password)
	db.session.add(new_user)
	db.session.commit()

def db_change_pw(username, password):
	user = User.query.filter(username=username)
	user.hashed_password = hash_plaintext_pw(password)
	db.session.commit()