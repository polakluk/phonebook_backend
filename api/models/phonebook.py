import json
import peewee
from backend import db

# model for table PhoneBook
class PhoneBook(peewee.Model):
	name = peewee.CharField(max_length = 32) # char field for name
	phone = peewee.CharField( max_length = 32) # char field for phone

	# JSON representation for serialization for response purposes
	def __repr__(self):
		return json.dumps({ 'name' : self.name, 'phone' : self.phone, 'id' : self.id })

	class Meta:
		database = db # This model uses the shared database.


# model for PhoneBook record in Session
class PhoneBookSession:

	def __init__(self):
		self.id = None
		self.name = None
		self.phone = None

	# JSON representation for serialization in SESSION
	def __repr__(self):
		return json.dumps({ 'name' : self.name, 'phone' : self.phone, 'id' : self.id})
