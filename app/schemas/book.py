from ..main import MA

# Book Schema
class BookSchema(MA.Schema):
  class Meta:
    fields = ('id', 'title', 'description', 'author', 'cover', 'price')

# Init schema
book_schema = BookSchema(strict=True)
books_schema = BookSchema(many=True, strict=True)
