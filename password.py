import re
import bcrypt


def is_valid_password(password):
	upper = r"[A-Z]"
	digit = r"[0-9]"
	special = r"[#?!@$%^&*-]"


def hash_plaintext_pw(plaintext_pw):
	return bcrypt.hashpw(plaintext_pw.encode(), bcrypt.gensalt())


def validate_password(plaintext_pw, hashed_pw):
	return bcrypt.checkpw(plaintext_pw, hashed_pw)

if __name__ == "__main__":
	print(hash_plaintext_pw("password"))
	print(validate_password("password".encode("utf-8"), hash_plaintext_pw("password")))