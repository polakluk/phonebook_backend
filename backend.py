from flask import Flask, g
from flask.ext.cors import CORS
from flask.ext.session import Session
import peewee

# just initialize our application
app = Flask(__name__)
CORS(app, resources={r"/phonebook/*": {"origins": "*"}})
app.config.from_object('config.Config')

Session(app)

# set up database and open up the connection
db = peewee.SqliteDatabase(app.config['DATABASE_URI'])
@app.before_request
def before_request():
    g.db = db
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response