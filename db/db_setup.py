from enum import unique
from locale import currency
import os
import configparser
from unicodedata import name
from sqlalchemy import Float, create_engine, func
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import csv

Base = declarative_base()

class Athlete(Base):
    __tablename__ = 'athletes'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    nationality = Column(String(64))
    currentrank = Column(Integer)
    prevyearrank= Column(Integer)
    sport= Column(String(64))
    year= Column(String(64))
    earnings= Column(Float)

config = configparser.ConfigParser()
config.read('../settings.conf')

dbconnect = config["MYSQL"]["CONNECTION_STRING"]
#dbconnect = 'mysql://root:password@localhost/athletes_data'

engine = create_engine(dbconnect, echo=True)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

Base.metadata.create_all(engine)

def checkNum(string):
    try:
        i=int(string)
    except:
        return True
    if (string== "  "):
        return True
    return False 

csvFile='../richathletes.csv'
with open(csvFile) as file:
    reader = csv.reader(file, csv)
    for row in reader:
        previousYearRank=0
        
        if checkNum(row[3]):
            previousYearRank=-1
        else:
            previousYearRank=row[3] 
        session.add(Athlete(name=row[0], nationality=row[1], currentrank=row[2], prevyearrank=previousYearRank, sport=row[4], year=row[5], earnings=row[6]))
    session.commit()