from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#configurations
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gleb:@localhost/prism'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
