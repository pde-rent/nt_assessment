from ..main import MA

# User Schema
class UserSchema(MA.Schema):
  class Meta:
    fields = ('id', 'name', 'hash')

# Init schema
user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)
