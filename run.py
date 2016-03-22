# this is entry point for the application

# import global object for this application
from backend import app, db

# import other parts of the application (other modules)
import api.models.phonebook
import api.views

# create tables, if you have to
def create_tables():
	list_tables = [api.models.phonebook.PhoneBook]

	db.create_tables(list_tables, safe = True)


# run the script
if __name__ == '__main__':
    create_tables()
    app.run(debug = True)