# import random to generate a list of random numbers
import random

# m is a multiplier, chose 1.25 which works well with float
m = 1.25

# create random list of range 1 to 1000, with 5 items
firstList = [float(i) for i in random.sample(range(1, 1000), 5)]
randomList = firstList[:]
print("initial list", randomList)

# This one does not affect the list
for item in randomList:
    item *= m
print("first try", randomList)

# This one does
randomList = firstList[:]
for index in range(len(randomList)):
    randomList[index] *= m
print("second try", randomList)

# This also does
randomList = firstList[:]
randomList = [i*m for i in randomList]
print("third try", randomList)
