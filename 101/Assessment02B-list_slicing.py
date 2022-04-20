#Matt Boughey
#CSCI 102 Section B
#Assessment 02B
#References: None
#Time: 20 minutes

sample = input("Enter your string\nString> ")
list1 = list(sample)

print("Enter four numbers to slice the string")
a = int(input("A> "))
b = int(input("B> "))
c = int(input("C> "))
d = int(input("D> "))
e = (a+1)
f = (c+1)
print("OUTPUT " + str(sample[e:b]), sample[f:d])
