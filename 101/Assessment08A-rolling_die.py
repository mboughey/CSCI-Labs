# Matt Boughey
# CSCI 102 Section B
# Assessment 08A
# References: None
# Time: 60-90 Minutes

import random
sides = int(input("Input the number of sides of the die:\nSIDES> "))
rolls = int(input("Input the number or rolls to make:\nROLLS "))
seed = int(input("Input the seed for the random number generator\nSEED "))
random.seed(seed)
# The below list is for all of the rolls results
allNums = []

# This loop creates the random roll, and adds that number to the list of numbers that have been rolled
for i in range(rolls):
    val = random.randint(1,sides)
    
    allNums.append(val)
allNums.sort()
print(f"Your {rolls} rolls of a {sides}-sided die follow:")

# This for loop prints the final inputs and counts the number of times each number is rolled
for i in range (sides):
    print("OUTPUT", str(i+1), "occurred", allNums.count(i+1), "times")



