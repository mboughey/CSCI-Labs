# Matt Boughey
# CSCI 102 B
# References: None
# Time: 15 Minutes


import random
nums = 0
file = open("dictionary.txt", "r")
length = int(input("Enter the length of the words to find:\nLENGTH> "))
seed = input("Enter the seed to use:\nSEED> ")
random.seed(seed)
list1 = []
for i in file:
    if len(i.strip()) == length:
        nums = nums + 1
        list1.append(i)
listLen = len(list1)
val = random.randint(0, listLen)
if val == 0:
    print(f"There are no words of length {length} in the dictionary")
    print("OUTPUT 0")
    print(f"The number of words with length {length}:")
    print("OUTPUT None")
    file.close()
    quit
else:
    
    word = list1[val]


    print(f"The number of words with length {length}:")
    print("OUTPUT", str(nums))
    print(f"Here is one random word with length {length}:")
    print(f"OUTPUT {word}")
    file.close()
    
