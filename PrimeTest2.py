import time
start_time = time.time()

upperBound = input("What number is the upper limit? ")
convertUpperBound = int(upperBound)
lowest = 0
primeList=[]

print ("Prime numbers:")

#Goes through every number from the lower to the upper bound
for number in range(lowest, convertUpperBound):
    #Checks that the number is above one so it can qualify as prime
    if number > 1:
        #Goes through every number from 1 to the current number
        for i in range(2, number):
            #If the number is not divisible only by one and itself, exit the if statement
            if (number % i) == 0:
                break
        #If the number is divisible by one and itself, add it to the array and print the array
        else:
            primeList.append(number)
print(primeList)
print(len(primeList))
print ("My program took " + str(time.time() - start_time) + " seconds to run.")
