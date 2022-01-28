from flask import Flask

from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)
app.config['SECRET_KEY'] = '34725824fedf7e6efd31e6bdc8f35902'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from FlaskPractice import routes