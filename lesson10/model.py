from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from db import *

Base = declarative_base()
 
class User(db.Model):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	username = Column(String)
	password = Column(String)


	def __init__(self, username, password):
		self.username = username
		self.password = password


class UserSchema(ma.Schema):
	class Meta:
		# Fields to expose
		fields = ('id', 'username')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


Base.metadata.create_all(engine)