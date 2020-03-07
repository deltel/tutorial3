from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ajdnfje98renerfu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:monster@localhost/db_app'
db = SQLAlchemy(app)

from app import views, models