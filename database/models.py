from database.shared import db
from sqlalchemy import Column, Date, DateTime, Integer, String, Sequence,ForeignKey
from datetime import datetime
from config import DB_CONNECT_STRING
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
	__tablename__ = "users"

	user_id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
	username = Column(String, index=True, nullable=False, unique=True)
	password_hash = Column(String, nullable=False)
	email = Column(String)
	created_date = Column(DateTime, default=datetime.utcnow)
	status = Column(String, default="ACTIVE")
	last_logged_in_date = Column(DateTime, default=datetime.utcnow)
	logged_in_count = Column(Integer, default=1)
	
	
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
		
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __init__(self, username, email):
		self.username = username
		self.email = email


#class LoginAudit(db.Model):
	# TO DO
	#pass
	
