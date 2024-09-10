import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from sqlalchemy.ext.declarative import declarative_base

load_dotenv() #load environment variable from the .env file

DATBASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATBASE_URL)
# create  a SQLAlchemy engine
# what is an sql alchemy engine?
# An engine is a factory for connection objects.it encapsulates a 
# connection pool that minimizes the cost of connecting to the 
# database by reusing existing connection and provide a consistent 
# API for working with transactions.
 
metadata = MetaData() # create a SQLAlchmy MetaData object

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# create aSQLAlchemy sessionmaker object

Base = declarative_base()

