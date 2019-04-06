from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
engine = create_engine('sqlite:///tutorial.db', echo=True)
