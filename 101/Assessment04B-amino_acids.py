#Matt Boughey
#CSCI102 Section B
#Assessment 04B
#References: None
#Time: 20 Minutes
print("Input the chemical elements of the amino acid:")
c = int(input("Carbon>"))
h = int(input("Hydrogen>"))
n = int(input("Nitrogen>"))
o = int(input("Oxygen>"))
s = int(input("Sulfur>"))
alanine = ("3C--7H--1N--2O--0S")
arginine =("6C--14H--4N--2O--0S")
asparagine = ("4C--8H--2N--3O--0S")
cysteine = ("3C--7H--1N--2O--1S")
histidine = ("6C--9H--3N--2O--0S")
glutamine = ("5C--10H--2N--3O--0S")
if c == 3:
    if s == 1:
        print(f"The amino acid for {cysteine} is Cysteine")
        print(f"OUTPUT {cysteine}")
        print("OUTPUT Cysteine")
    else:
        print(f"The amino acid for {alanine} is Alanine")
        print(f"OUTPUT {alanine}")
        print("OUTPUT Alanine")
if c == 6:
    if h == 14:
        print(f"The amino acid for {arginine} is Arginine")
        print(f"OUTPUT {arginine}")
        print("OUTPUT Arginine")
    else:
        print(f"The amino acid for {histidine} is Histidine")
        print(f"OUTPUT {histidine}")
        print("OUTPUT Histidine")
if c == 4:
    print(f"The amino acid for {asparagine} is Asparagine")
    print(f"OUTPUT {asparagine}")
    print("OUTPUT Asparagine")
if c == 5:
        print(f"The amino acid for {glutamine} is Glutamine")
        print(f"OUTPUT {glutamine}")
        print("OUTPUT Glutamine")
