import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

# Db initialization
database = SQLAlchemy()

# Connect to the db
engine = db.create_engine(SQLALCHEMY_DATABASE_URI)
connection = engine.connect()

# Create session object
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

metadata = db.MetaData()
# Define the tables
table_users = db.Table('users', metadata, autoload=True, autoload_with=engine)
table_buckets = db.Table('buckets', metadata, autoload=True, autoload_with=engine)