from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from local_config import DATABASE_CONFIG

app = Flask(__name__)

app.config['SQL_ALCHEMY_DATABASE_URI'] = DATABASE_CONFIG
db = SQLAlchemy()

with app.app_context():
    db.create_all()

