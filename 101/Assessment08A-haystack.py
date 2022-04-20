# Matt Boughey
# CSCI 102 Section B
# Assessment 08B
# References: None
# Time: 60 Minutes
'''
s = input("Enter a DNA string S:\nS> ")
t = input("Enter a substring T:\nT> ")
if len(t) > len(s):
    print("Error: Substring is longer than DNA string")
    print("OUTPUT ERROR")
    quit
else:
    pie = 1
occurrences = 0
count = 0
bruh = 0
positions = []






for i in range (len(s)):
    x = s.find(t, i)
    if x != -1:
        occurrences = occurrences + 1
        positions.append(x+1)
        count = count + 1










        
final = []
for i in range (len(positions)):
    if positions[i] not in final:
        final.append(positions[i])
    else:
        pie = 0
fin = len(final)
new = ""
for i in final:
    new = new + ' ' + str(i)
print(f"The total number of substrings found is {fin}")
print("The locations of these substrings in S are: ") and print(*final, sep=" ")
print(f'OUTPUT {fin}')
print(f"OUTPUT {new}")
'''



















k = ['A','E','I','O','U']
s = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z',]

occurrences = 0
count = 0














def init():
    print("Enter a string for the game:")
    st = input("STRING> ")
    pos = ''
    for i in range (len(st)):  
        if i in k:
            pos = str(k[i])
            break
        break
    prov(pos, st)




def prov():
    print("Enter a string for the game:")
    string = input("STRING> ")
    pos1 = ''
    global kscore
    kscore = 0
    
    count = 0
    while count != (len(string)):

        
        for i in range (len(string)):
            x = string.find(pos1, i)
            if x != -1:
                kscore = kscore + 1
                count = count + i
                break
        x = string.find(pos1 )
        if x != -1:
            kscore = kscore + 1
            count = count + 1
            print(pos1)
            pos1 = pos1 + str(string[i+1])
            
            


print("Would you like to provide your own string or generate a random one? (1 or 2)")
choice = int(input("CHOICE> "))

if choice == 1:
    prov()
if choice == 2:
    gen()




#print(f"Kevin: {kscore}")






























