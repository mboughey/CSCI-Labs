# Matt Boughey
# CSCI 102 B
# Assessment 06A
# References: None
# Time: 8 Minutes

mult = []
print("Enter the number to create multiples for.")
base = int(input("NUMBER> "))
print("Enter the maximum index of the list")
length = int(input("INDEX> "))
for i in range (length + 1):
    new = base * (i+ 1)
    mult.append(new)











factors = []

fct = max(mult)
for i in mult:
    
    for j in range (1, i):
        if i % j == 0:































            factors.append(i)
fin = []

for i in range(len(factors)):
    if factors[i] not in fin:
        fin.append(factors[i])


    








print(fct)
print("Your list of multiples is as follows:")
print(f"OUTPUT {mult}")
print("The last multiple calculated is:")
print(f"OUTPUT {mult[-1]}")

print(fin)

    
             
