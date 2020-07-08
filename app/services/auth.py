from argon2 import PasswordHasher

PH = PasswordHasher()

def hash(s: str) -> str:
	return PH.hash(s)

def hash_match(clear: str, hashed: str) -> bool:
	return PH.hash(clear) == hashed
