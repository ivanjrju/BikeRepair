from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  Column, Integer, String, Boolean

# local
# PATH = 'postgresql://postgres:postgres@localhost/bikerepair'

# Heroku
PATH = 'postgres://upgiusttrivecz:3b66b747df53cd9b4a5400aafe3d8ade87700be26ca00104ed89e1466e5d413e@ec2-54-235-208-103.compute-1.amazonaws.com:5432/dfhi7hgvmpvr1r'

App = Flask(__name__)
App.config['SQLALCHEMY_DATABASE_URI'] = PATH
db = SQLAlchemy(App)

from ErrorHandlers import *
from Routes import *

if __name__ == '__main__':
    App.run(host="0.0.0.0", port=80, debug='true')