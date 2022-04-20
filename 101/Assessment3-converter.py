# Matt Boughey
# CSCI101 Section B
# Python Assessment 3
# References: None
# Time: 50 Minutes

def dec():
    dec = 0
    exp = 0
    base2 = list(input("BINARY-STR> "))
    if base2 == 0:
        print("OUTPUT 0")
        quit
    for i in reversed(base2):
        add = int((int(i) * (2**exp)))
        dec = int(dec) + int(add)
        exp = exp + 1
    print("OUTPUT " + str(dec))

def binary():
    ctr = ""
    base10 = int(input("DECIMAL-STR> "))
    if base10 == 0:
        print("OUTPUT 0")
    else:
        while base10 != 0:
            x = str(base10 % 2)
            ctr = ctr + x
            base10 = base10 //2
        final = ctr[::-1]
        print("OUTPUT " + final)
        
print("Welcome to the Binary-Decimal Converter")
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
print("Enter an Option:\n1. Binary-Decimal Conversion\n2. Decimal-Binary Conversion")
choice = int(input("OPTION> "))

if choice == 1:
    dec()
if choice == 2:
    binary()

