# Matt Boughey
# CSCI101 B
# Assessment 06B
# Time: way too long
# References: None
counter = 0

print("How many numbers am I estimating John?")
count = int(input("COUNT> "))
initGuess = 11

nums = []

for i in range (count):
    val = float(input("NUMBER> "))
    nums.append(val)

for i in range (len(nums)):
    betterGuess = 10
    counter = 0
    while initGuess != betterGuess:
        initGuess = betterGuess
        counter = counter + 1

        betterGuess = (initGuess + nums[i]/initGuess)/2
    print("OUTPUT After", counter, "iterations,", str(nums[i]) + "^0.5 = {:.2f}".format(initGuess))
    
