from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  Column, Integer, String, Boolean


PATH = 'postgresql://postgres:postgres@localhost/bikerepair'

App = Flask(__name__)
App.config['SQLALCHEMY_DATABASE_URI'] = PATH
db = SQLAlchemy(App)

from ErrorHandlers import *
from Routes import *

if __name__ == '__main__':
    App.run(host="0.0.0.0", port=80, debug='true')