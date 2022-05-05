from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import configparser

class DbConnect:   

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('settings.conf')

        # Engine is the core interface to the database
        dbconnect = self.config["MYSQL"]["CONNECTION_STRING"]
        engine = create_engine(dbconnect, echo=True)

        # Create a database session, bind to the engine and prepare to use
        Session = sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()

    def Session(self):
        return self.session