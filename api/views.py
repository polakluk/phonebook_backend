# import main app object
from backend import app

# import other modules
from flask import session
from flask_restful import Api
from resources import phonebook

api = Api(app)

# import resources
api.add_resource(phonebook.PhoneBook, '/phonebook')


# ordinary routes

# route for testing work with session
@app.route('/test')
def test():
	val = session.get('value', None)
	if val == None:
		val = 1
	else:
		val += 1

	session['value'] = val
	return "Current Result = " + str(val)