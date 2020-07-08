from main import DB, MA, APP
from flask import request as req
from flask import Response as Rep
from services.store import save_cover
from models.book import Book
from models.user import User
from services import serialize

# ACCESS: PUBLIC
# Used by anyone to get a filtered list of books
@APP.route('/api/books', methods=['GET'])
def get_books():
	# TODO: check whether the req parameters are all passed and valid!
	title = req.args.get('title')
	author = req.args.get('author')
	min_price = req.args.get('min_price')
	max_price = req.args.get('max_price')
	# TODO: check for result availability and manage error cases
	result = Book.get(title, author, min_price, max_price)
	return serialize.respond(req, result)

# ACCESS: PUBLIC
# Used by authors to log in the bookstore
@APP.route('/api/login', methods=['POST'])
def login():
	# TODO: check whether the req parameters are all passed and valid!
	user_name = req.args.get('user_name')
	password = req.args.get('pass')
	if not user_name or not password:
		return forbidden_header();
	user = User('user_name')
	if isinstance(user, User) and user.login(password):
		session['user_name'] = user.name
		return success_header();
	return forbidden_header()

# ACCESS: ONLY AUTH
# Used by authors to publish a book >> not asked
@APP.route('/api/publish', methods=['POST'])
def publish():
	user_name = session.get('user_name')
	if not user_name:
		return forbidden_header()
	user = User(user_name)
	if (user.logged_in):
		return forbidden_header()
	# TODO: check whether the req parameters are all passed and valid!
	title = req.args.get('title')
	description = req.args.get('description')
	author = req.args.get('author')
	# cover_image = req.files.get('cover', '')
	cover_image = req.files['cover_image']
	cover = save_cover(cover_image)
	price = req.args.get('price')

	Book.save(Book(title, description, author, cover, price))
	# TODO: check status error
	return success_header()

# ACCESS: ONLY AUTH
# Used by authors to unpublish a book
@APP.route('/api/unpublish', methods=['DELETE'])
def unpublish():
	# TODO: check whether the req parameters are all passed and valid!
	title = req.args.get('title')
	author = req.args.get('author')
	Book.remove(title, author)
	# TODO: check status error
	return success_header()

def forbidden_header():
	return json.dumps({'success':False}), 403, {'ContentType':'application/json'})

def success_header():
	return json.dumps({'success':True}), 200, {'ContentType':'application/json'})
