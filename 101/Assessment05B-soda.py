# MAtt Boughey
# CSCI102 B
# Assessment 05B
# References: None
# Time: 5 Minutes

empty = int(input("Enter the number of empty bottles in Blaster's possesion at the start of the day.\nEMPTIES> "))
found = int(input("Enter the number of empty bottles the Blaster found during the day.\nFOUND> "))
cost = int(input("Enter the number of empty soda bottles required to buy a new soda.\nCOST> "))
drank = 0
empty = empty + found
while empty >= (cost):
    empty = empty - cost
    drank = drank + 1
    empty = empty + 1
print("The total number of sodas that blaster drank is:")
print(f"OUTPUT {drank}")
