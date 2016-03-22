from flask_restful import Resource
from flask import session
from flask_restful import reqparse
from peewee import IntegrityError

from api.models import phonebook

# API Resource to work with PhoneBook
class PhoneBook(Resource):

	# GET request
    def get(self):
    	# get request data
		parser = reqparse.RequestParser()
		parser.add_argument('name')
		parser.add_argument('id', type=int)
		parser.add_argument('list_limit', type=int, default=5)
		parser.add_argument('list_page', type=int, default=1)
		args = parser.parse_args()

		# was name of the record specified?
		result = {'error' : False, 'msg' : '', 'data' : '', 'total' : 0}
		if args['name'] == None:
			if args['id'] == None: # was ID specified
				# no, the name was not specified (neither was ID), so get the whole list
				data = []
				if args['list_limit'] > 0:
					dataDb = phonebook.PhoneBook.select().paginate(args['list_page'], args['list_limit']);
				else:
					dataDb = phonebook.PhoneBook.select()

				for row in dataDb:
					data.append(str(row))

				if len(data) == 0:
					result['msg'] = 'No records'
				else:
					result['total'] = phonebook.PhoneBook.select().count()

				result['data'] = data
			else:
				# yes, ID was specified so get the record
				try:
					result['data'] = [str(phonebook.PhoneBook.get(id=args['id']))]
				except phonebook.PhoneBook.DoesNotExist:
					# no record with this name was foun
					result['error'] = True
					result['msg'] = "No record found"

		else:
			# yes, so try to find the record
			try:
				result['data'] = [str(phonebook.PhoneBook.get(name=args['name']))]
			except phonebook.PhoneBook.DoesNotExist:
				# no record with this name was foun
				result['error'] = True
				result['msg'] = "No record found"

		return result



    # POST request
    # this method will store provided information into currently opened Session
    def post(self):
    	# get request data
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str)
		parser.add_argument('phone', type=str)
		args = parser.parse_args()

		# store them in session
		record = phonebook.PhoneBookSession()
		record.name = args['name']
		record.phone = args['phone']
		session['record'] = record
		return session['record']

    # PUT request
    def put(self):
    	# get request data
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str)
		parser.add_argument('phone', type=str)
		args = parser.parse_args()

		# store them in session
		record = phonebook.PhoneBook()
		record.name = args['name']
		record.phone = args['phone']

		try:
			record.save()
		except IntegrityError: # if saving the record fails, inform client about it
			return {'id' : '', 'error' : True}

		return {'id' : record.id, 'error' : False}