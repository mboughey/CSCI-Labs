#Matt Boughey
#CSCI 102 Section B
#Assessment 03B
#References: None
#Time: 15 Minutes

print("Welcome to out enhanced calculator!")
num1 = float(input("Input the first operand\nFIRST> "))
num2 = float(input("Input the second operand\nSECOND> "))

choice = input("Choose one of the following operations:\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\nOPERATION> ")











def add():
    sum = num1 + num2
    sum1 = round(sum, 1)
    print("The result of the addition is {:.6f}".format(sum1))
    print("OUTPUT {:.6f}".format(sum1))

def subtract():
    diff = num1 - num2
    
    print("The result of the subtraction is {:.6f}".format(diff))
    print("OUTPUT {:.6f}".format(diff))

def product():
    prod = num1 * num2
    prod1 = round(prod, 1)
    print("The result of the multiplication is {:.6f}".format(prod1))
    print("OUTPUT {:.6f}".format(prod1))
    
def divide():
    quot = int(num1 // num2)
    
    rem = int(num1 % num2)
    

    
    print(f"The result of the division is: {quot} (Quotient) and {rem} (remainder)")
    print("OUTPUT", quot)
    print("OUTPUT", rem)








    
def remainder():
    rem = num1 % num2
    rem1 = round(rem, 2)
    print("The remainder of " + str(num1) + " and " + str(num2) + " is {:.2f}".format(rem1))
    print("OUTPUT {:.6f}".format(rem1))



def selection():
    
    if choice == "1":
        add()
    if choice == "2":
        subtract()
    if choice == "3":
        product()
    if choice == "4":
        divide()



selection()
