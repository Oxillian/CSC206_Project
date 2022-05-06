from crypt import methods
from email.mime import base
from re import I
from this import d
from MySQLdb import connect
from flask import Flask, request, render_template, redirect, session, url_for, jsonify
from enum import unique
import os
from os.path import join, dirname, realpath
from datetime import datetime
#import pandas as pd
import csv
import configparser
from pymysql import Connect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import Float, create_engine, func, select
import numpy
import matplotlib.pyplot as plt
from pprint import pprint
from matplotlib.pyplot import figure


#Table model
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
#Read db connection string
config = configparser.ConfigParser()
config.read('./settings.conf')

dbconnect = config["MYSQL"]["CONNECTION_STRING"]
#dbconnect = 'mysql://root:password@localhost/athletes_data'#Connect to db
engine = create_engine(dbconnect, echo=True)
#Create session
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

app = Flask(__name__)

@app.route('/')
def index():
    welcomeMessage="Hello, please go to /americanathletes, /1athletes, /moneybysport, or /peopleincountry by clicking one of the links above"
    
    return render_template("csv.html", athleteData=welcomeMessage)

@app.route('/americanathletes', methods=['GET'])
def americanAthletes():
    athleteData = session.query(Athlete).filter_by(nationality= "USA").all()
    rowName=[]
    rowNationality=[]
    rowSport=[]
    rowYear=[]

    pieNames='Boxing', 'Golf', 'Basketball', 'Tennis', 'NFL', 'Baseball', 'American Football/Baseball', 'NASCAR', 'Cycling'
    boxing=0
    golf=0
    basketball=0
    tennis=0
    nfl=0
    baseball=0
    americanFootBallBaseball=0
    nascar=0
    cycling=0
    pieAmounts=[]
    explode= (0, 0, 0, 0, 2, 1.5, 1.6, 2, 0)
    labels=list(pieNames)

    
    for row in athleteData:
        #rows.append(row.name + " " + row.nationality + " " + row.sport + " " + row.year)
        rowName.append(row.name)
        rowNationality.append(row.nationality)
        rowSport.append(row.sport)
        rowYear.append(row.year)
        lengths=len(athleteData)
        #Could put in function. Starts graph section
        if row.sport=='Boxing':
            boxing+=1
        if row.sport=='Golf':
            golf+=1
        if row.sport=='Basketball':
            basketball+=1
        if row.sport=='Tennis':
            tennis+=1
        if row.sport=='NFL':
            nfl+=1
        if row.sport=='Baseball':
            baseball+=1
        if row.sport=='American Football / Baseball':
            americanFootBallBaseball+=1
        if row.sport=='NASCAR':
            nascar+=1
        if row.sport=='Auto Racing':
            nascar+=1
        if row.sport=='Auto Racing (Nascar)':
            nascar+=1
        if row.sport=='Cycling':
            cycling+=1
    pieAmounts.append(boxing)
    pieAmounts.append(golf)
    pieAmounts.append(basketball)
    pieAmounts.append(tennis)
    pieAmounts.append(nfl)
    pieAmounts.append(baseball)
    pieAmounts.append(americanFootBallBaseball)
    pieAmounts.append(nascar)
    pieAmounts.append(cycling)    

    fig1, ax1 = plt.subplots()
    ax1.pie(pieAmounts, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
    ax1.axis('equal')
    plt.savefig("static/piechart.png")
    
    return render_template("csv2.html", lengths=lengths, athleteName=rowName, athleteNationality=rowNationality, athleteSport=rowSport, athleteYear=rowYear)
        
@app.route('/1athletes', methods=['GET'])
def numberOnes():
    print("athletes who are currently ranked 1")
    athleteData = session.query(Athlete).filter_by(currentrank= "1").all()
    rowName=[]
    rowRank=[]
    rowPRank=[]
    rowSport=[]
    rowYear=[]
    #athletesR1=[]
    for athletes in athleteData:
        #pprint(athletes.name + " " + athletes.nationality + " " + str(athletes.currentrank) + " " + str(athletes.prevyearrank) + " " + athletes.sport)
        #athletesR1.append(athletes.name + " " + str(athletes.currentrank) + " " + str(athletes.prevyearrank) + " " + athletes.sport + " " + athletes.year)
        rowName.append(athletes.name)
        rowRank.append(athletes.currentrank)
        rowPRank.append(athletes.prevyearrank)
        rowSport.append(athletes.sport)
        rowYear.append(athletes.year)
        lengths=len(athleteData)
            #or print(db.session.query(Athlete)) or full(from above)
            #or copy line 48: full=row.query.filter_by(currentrank= '1').all()
            #need to append it to new list
    return render_template("csv3.html", lengths=lengths, athleteName=rowName, athleteRank=rowRank, athletePRank=rowPRank, athleteSport=rowSport, athleteYear=rowYear)

@app.route('/moneybysport', methods=['GET'])
def sportMoney():
    athleteData = session.query(Athlete)
    
    boxing=0.0
    autoRacing=0.0
    golf=0.0
    basketball=0.0
    nfl=0.0
    tennis=0.0
    baseball=0.0
    iceHockey=0.0
    americanFootballBaseball=0.0
    f1Motorsports=0.0
    cycling=0.0
    motorcycleGP=0.0
    soccer=0.0
    earnings=[]

    for row in athleteData:
        if row.sport=="Boxing":
            boxing+=row.earnings
            
        if row.sport=="Auto Racing":
            autoRacing+=row.earnings
            
        if row.sport=="Golf":
            golf+=row.earnings
            
        if row.sport=="Basketball":
            basketball+=row.earnings
            
        if row.sport=="NFL":
            nfl+=row.earnings
            
        if row.sport=="Tennis":
            tennis+=row.earnings
            
        if row.sport=="Baseball":
            baseball+=row.earnings
            
        if row.sport=="Ice Hockey":
            iceHockey+=row.earnings
            
        if row.sport=="American Football / Baseball":
            americanFootballBaseball+=row.earnings
            
        if row.sport=="F1 Motorsports":
            f1Motorsports+=row.earnings
            
        if row.sport=="Cycling":
            cycling+=row.earnings
            
        if row.sport=="Motorcycle GP":
            motorcycleGP+=row.earnings
            
        if row.sport=="Soccer":
            soccer+=row.earnings
            
    
    earnings.append(boxing)
    earnings.append(autoRacing)
    earnings.append(golf)
    earnings.append(basketball)
    earnings.append(nfl)
    earnings.append(tennis)
    earnings.append(baseball)
    earnings.append(iceHockey)
    earnings.append(americanFootballBaseball)
    earnings.append(f1Motorsports)
    earnings.append(cycling)
    earnings.append(motorcycleGP)
    earnings.append(soccer)
    earnings.sort()

    lengths=len(earnings)
    return render_template('csv4.html', lengths=lengths, athleteData=earnings, boxing=boxing, autoRacing=autoRacing, golf=golf, basketball=basketball, nfl=nfl, tennis=tennis, baseball=baseball, iceHockey=iceHockey, americanFootballBaseball=americanFootballBaseball, f1Motorsports=f1Motorsports, cycling=cycling, motorcycleGP=motorcycleGP, soccer=soccer)

@app.route('/peopleincountry', methods=['GET'])
def peopleCountry():
    athleteData = session.query(Athlete)

    usa=0
    brazil=0
    france=0
    australia=0
    canada=0
    uk=0
    austria=0
    germany=0
    russia=0
    italy=0
    finland=0
    switzerland=0
    philippines=0
    portugal=0
    dominican=0
    argentina=0
    filipino=0
    spain=0
    serbia=0
    ireland=0
    mexico=0
    people=[]
    
    pieNames='USA', 'Brazil', 'France', 'Australia', 'Canada', 'UK', 'Austria', 'Germany', 'Russia', 'Italy', 'Finland', 'Switzerland', 'Philippines', 'Portugal', 'Dominican', 'Argentina', 'Filipino', 'Spain', 'Serbia', 'Ireland', 'Mexico'
    labels=list(pieNames)
    explode= (0, 1, 0, 1.5, 1.5, 2, 1, 2.5, 1, 2, 1, 3, 1, 2, 1, 2.2, 0, 2.4, 2.6, 2.8, 3)
    pieAmounts=[]

    for row in athleteData:
        if row.nationality=="USA":
            usa+=1
            
        if row.nationality=="Brazil":
            brazil+=1
            
        if row.nationality=="France":
            france+=1
            
        if row.nationality=="Australia":
            australia+=1
            
        if row.nationality=="Canada":
            canada+=1
            
        if row.nationality=="UK":
            uk+=1
            
        if row.nationality=="Austria":
            austria+=1
            
        if row.nationality=="Germany":
            germany+=1
            
        if row.nationality=="Russia":
            russia+=1
            
        if row.nationality=="Italy":
            italy+=1
            
        if row.nationality=="Finland":
            finland+=1
            
        if row.nationality=="Switzerland":
            switzerland+=1
            
        if row.nationality=="Philippines":
            philippines+=1
        
        if row.nationality=="Portugal":
            portugal+=1

        if row.nationality=="Dominican":
            dominican+=1

        if row.nationality=="Argentina":
            argentina+=1

        if row.nationality=="Filipino":
            filipino+=1

        if row.nationality=="Spain":
            spain+=1

        if row.nationality=="Serbia":
            serbia+=1

        if row.nationality=="Northern Ireland":
            ireland+=1

        if row.nationality=="Ireland":
            ireland+=1

        if row.nationality=="Mexico":
            mexico+=1
    
    people.append(usa)
    people.append(brazil)
    people.append(france)
    people.append(australia)
    people.append(canada)
    people.append(uk)
    people.append(austria)
    people.append(germany)
    people.append(russia)
    people.append(italy)
    people.append(finland)
    people.append(switzerland)
    people.append(philippines)
    people.append(portugal)
    people.append(dominican)
    people.append(argentina)
    people.append(filipino)
    people.append(spain)
    people.append(serbia)
    people.append(ireland)
    people.append(mexico)
    people.sort()
    lengths=len(people)
    
    pieAmounts.append(usa)
    pieAmounts.append(brazil)
    pieAmounts.append(france)
    pieAmounts.append(australia)
    pieAmounts.append(canada)
    pieAmounts.append(uk)
    pieAmounts.append(austria)
    pieAmounts.append(germany)
    pieAmounts.append(russia)
    pieAmounts.append(italy)
    pieAmounts.append(finland)
    pieAmounts.append(switzerland)
    pieAmounts.append(philippines)
    pieAmounts.append(portugal)
    pieAmounts.append(dominican)
    pieAmounts.append(argentina)
    pieAmounts.append(filipino)
    pieAmounts.append(spain)
    pieAmounts.append(serbia)
    pieAmounts.append(ireland)
    pieAmounts.append(mexico)
    print(pieAmounts)

    fig1, ax1 = plt.subplots()
    ax1.pie(pieAmounts, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
    ax1.axis('equal')
    fig1.set_size_inches(14.5, 6.5)
    plt.savefig("static/piechart2.png")

    return render_template('csv5.html', lengths=lengths, athleteData=people, usa=usa, brazil=brazil, france=france, australia=australia, canada=canada, uk=uk, austria=austria, germany=germany, russia=russia, italy=italy, finland=finland, switzerland=switzerland, philippines=philippines, portugal=portugal, dominican=dominican, argentina=argentina, filipino=filipino, spain=spain, serbia=serbia, ireland=ireland, mexico=mexico)


#SQL sum/avg functions?
#group by? Descending? order by?
#https://www.geeksforgeeks.org/switch-case-in-python-replacement/

#Part 6
#avg earnings by sport. pie chart athletes by sport(12% racing). total earnings pie chart by sport
#https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_href_anchor
