import os

class Config:
	# define base path
	BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

	# configurate sqlite db location
	DATABASE_URI = os.path.join(BASE_DIR, 'db.sqlite')
	
	# select session type
	SESSION_TYPE = "filesystem"

	# session location
	SESSION_FILE_DIR = os.path.join(BASE_DIR, '_sessions')