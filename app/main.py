from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

# Init app
APP = Flask(__name__)
APP.config['ROOT_DIR'] = os.path.abspath(os.path.dirname(__file__))
APP.config['COVER_DIR'] = os.path.join(APP.config['ROOT_DIR'], "store", "covers")
# Database
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(APP.config['ROOT_DIR'], 'db.sqlite')
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
APP.config['SESSION_TIMEOUT'] = 60 * 15 # 15 minutes
# Init db
DB = SQLAlchemy(APP)
# Init ma
MA = Marshmallow(APP)

if __name__ == '__main__':
	APP.run(debug=True)
