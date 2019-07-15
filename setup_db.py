from app import app
from models import User
from flask_sqlalchemy import SQLAlchemy


if __name__ == "__main__":
	db = SQLAlchemy(app)
	admin = User("admin", "admin@admin.com")
	admin.set_password("password")
	guest = User("guest", "guest@guest.com")
	guest.set_password("guest")
	db.session.add(admin)
	db.session.add(guest)
	db.session.commit()