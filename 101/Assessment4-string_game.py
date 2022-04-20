



k = ['A','E','I','O','U']
s = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z',]

occurrences = 0
count = 0


import random
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


word = ""




print("Would you like to provide your own string or generate a random one? (1 or 2)")
choice = int(input("CHOICE> "))

if choice == 1:
    print("Enter a string for the game:")
    string = input("STRING> ")
if choice == 2:
    print("Number to initialize the random generator:")
    seed = int(input("SEED> "))
    random.seed(seed)







    letInd = random.random() * len(alphabet)
    word+= alphabet[int(letInd)]

    print(word)

for i in range (len(string)):
    if string[i] in k:
        word = string[i]
        break
    
    





'''
count = 0


for i in range (len(string)):
    x = string.find(word, i)
    if x != -1:
        occurrences = occurrences + 1
        count = count + 1




'''








































'''

def prov():
    print("Enter a string for the game:")
    string = input("STRING> ")
    pos1 = ''
    global Sscore
    Sscore = 0
    count2 = 0
    pos2 = ''
    global kscore
    kscore = 0
    
    count = 0
    #for i in range (len(string)):
    while True:
        
        for i in range (len(string)):
            x = string.find(pos1, i)
            if x != -1:
                kscore = kscore + 1
                count = count + 1
            if x != -1:
                kscore = kscore + 1
                count = count + 1
                print(pos1)
                pos1 = pos1 + str(string[i+1])



    while True:
        
        for i in range (len(string)):
            x = string.find(pos2, i)
            if x != -1:
                kscore = kscore + 1
                count = count + 1
            if x != -1:
                kscore = kscore + 1
                count = count + 1
                print(pos1)
                pos1 = pos1 + str(string[i+1])
                


            


print(f"Kevin: {kscore}")

'''

