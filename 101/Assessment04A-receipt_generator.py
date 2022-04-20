#Matt Boughey
#CSCI102 - Section B
#Assessment04A
#References: None
#Time: 30 Minutes

name = input("Enter Company name: ")
city = input("Enter company city/state: ")
cashier = input("Enter cashier name: ")
item1N = input("Purchased item 1 name: ")
item1P = input("Purchased item 1 price: ")
item2N = input("Purchased item 2 name: ")
item2P = input("Purchased item 2 price: ")
item3N = input("Purchased item 3 name: ")
item3P = input("Purchased item 3 price: ")
message = input("Enter your favorite ending message: ")
cost = float(item1P) + float(item2P) + float(item3P)
title = "RECEIPT GENERATOR"
print(title.center(30))
print("------------------------------")
print(name.center(30))
print(city.center(30))
print("==============================")
cashier = (f"Your cashier was: {cashier}")
print(str(cashier).center(30))
print(("Welcome Valued Customer").center(30))
print("==============================")
print(("Item Name").center(15) + ("Item Price").center(15))
print((item1N).center(15) + ("$" + item1P).center(15))
print((item2N).center(15) + ("$" + item2P).center(15))
print((item3N).center(15) + ("$" + item3P).center(15))
print("==============================")
cost = round(cost, 2)
cost = str(cost)
c = (f"Total cost of order: ${cost}")
print((str(c).center(30)))
print("==============================")
print(message.center(30))
print("------------------------------")
