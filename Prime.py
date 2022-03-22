from flask import Flask, render_template, request
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def index2():

    """ upperBound = input("What number is the upper limit? ") """
    """ form_data=request.form
    upperBound=form_data """
    upperBound=request.form.get("number")
    
    
    start_time=time.time()
    convertToString=int(upperBound)

    
    
    lowest = 0
    primeList=[]
    """ firstTen= primeList[:10]
    lastTen=primeList[-10:] """

    print ("Prime numbers:")

    #Goes through every number from the lower to the upper bound
    for number in range(lowest, convertToString):
        #Checks that the number is above one so it can qualify as prime
        if number > 1:
            #Goes through every number from 1 to the current number
            for i in range(2, number):
                #If the number is not divisible only by one and itself, exit the if statement
                if (number % i) == 0:
                    break
                #If the number is divisible by one and itself, add it to the array and print the array. If the else is lined up with the for, firstTen@bottom needs to be primeList[:10], if lined up with 2nd if, weird stuff happens
            else:
                primeList.append(number)
                if len(primeList)<20:
                    list2=primeList
                else:
                    firstTent=primeList[:10]
                    lastTent=primeList[-10:]
    """ print(primeList)
    print("Number of prime numbers: " + str(len(primeList)))
    print ("My program took " + str(time.time() - start_time) + " seconds to run.") """
    return render_template('primeList.html', number=upperBound, list=primeList, time=start_time, list2=list2, firstTen=primeList[:10], lastTen=primeList[-10:])
