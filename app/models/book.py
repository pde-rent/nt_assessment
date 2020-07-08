from ..main import DB, APP
from ..schemas.book import book_schema, books_schema
from sys import float_info

# Book Class/Model
class Book(DB.Model):

	__tablename__ = 'books'

	id = DB.Column(DB.Integer, primary_key=True)
	title = DB.Column(DB.String(512), unique=False)
	description = DB.Column(DB.String(2048), unique=False)
	author = DB.Column(DB.String(512), unique=False)
	cover = DB.Column(DB.String(512), unique=False) # filename of the cover in fs://.../store/covers/ >> can easily be optimized
	price = DB.Column(DB.Float)

	def __init__(self, title, description, author, cover, price):
		self.title = title
		self.description = description
		self.author = author
		self.cover = cover
		self.price = price

	def __repr__(self):
		return f"<Book(title='{self.title}', description='{self.description}', author='{self.author}', cover='{self.cover}, price='{self.price}')>"
	
	# CRUD implementations
	# TODO: use Schema(only=("attr1", "attr2")) and Schema(exclude=("attr1", "attr2")) to allow partial entity response

	@staticmethod
	def remove(title, author):
		book = book_schema.load({"title" : title, "author": author})
		if isinstance(book, Book):
			DB.session.delete(book)
			DB.session.commit()

	@staticmethod
	def save(book):
		DB.session.add(book)
		DB.session.commit()

	@staticmethod
	def get_all():
		unfiltered = Book.query.all()
		# filter the fields out
		return books_schema.dump(unfiltered)

	# TODO: this is definately unoptimized. the filtering should occur
	# when the SELECT is executes by sqlAlchemy by Marshmello load() method.
	# I did not have the time to look into this further
	@staticmethod
	def get(titles = [], authors = [], min_price = 0, max_price = float_info.max):
		books = Book.get_all()
		for b in books:
			if (len(titles) > 0):
				if b.title not in titles:
					books.remove(b)
			elif (len(authors) > 0):
				if b.author not in authors:
					books.remove(b)
			elif b.price < min_price or b.price > max_price:
				books.remove(b)
		return books
