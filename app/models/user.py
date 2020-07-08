from ..main import DB, APP
from ..schemas.user import user_schema, users_schema
from ..services import auth
from datetime import datetime

# User Class/Model
class User(DB.Model):

	__tablename__ = 'users'

	id = DB.Column(DB.Integer, primary_key=True)
	name = DB.Column(DB.String(512), unique=False)
	hash = DB.Column(DB.String(256), unique=False)
	logged_in = DB.Column(DB.Boolean, unique=False)
	login_time = DB.Column(DB.DateTime, unique=False)

	def __init__(self, name):
		self.name = name
	
	def __repr__(self):
		return f"<User(name='{self.name}'>"

	@staticmethod
	def login(self, password):
		self = user_schema.load({"name": self.name})
		if isinstance(self, User) and auth.hash_match(password, self.hash):
			self.logged_in = True
			self.login_time = datetime.now()
			DB.session.commit()
			return True
		return False

	def is_logged_in(self):
		self = user_schema.load({"name": self.name})
		if (self.logged_in):
			if (datetime.now() - self.login_time).total_seconds() > APP.config["SESSION_TIMEOUT"]:
				self.logged_in = False
				DB.session.commit()
				return False
			return True
		return False
