# Example back-end application for phonebook application

This application is written in Python 2.7.11 and using following modules:

* Flask 0.10.1.
* Peewee 2.8.0
* Flask Restful 0.3.5
* Flask Session 0.2.3
* Flask CORS 2.1.2

# How to install

Here is list of commands which install them to your environment:

```
pip install flask
pip install peewee
pip install flask-restful
pip install flask-session
pip install flask-cors
```

# How to run

In order to run the application, run following command from commmand-line while being in the root directory of the application:

```
python ./run.py
```
Then, you can query the server on address http://localhost:5001. The application will create its sqlite database, if file db.sqlite file in the root directory. Name of this file can be customized in fily config.py. Also, port number can be customizes in config.py.
