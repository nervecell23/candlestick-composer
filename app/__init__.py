import os
from flask import Flask
from flask_migrate import Migrate
from app.models import db

corr_app = Flask(__name__)
curr_env = os.environ.get('FLASK_ENV', None)

if curr_env == 'development':
    corr_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI_DEV']
elif curr_env == 'production':
    corr_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI'] 
corr_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(corr_app)
migrate = Migrate(app=corr_app, db=db)



