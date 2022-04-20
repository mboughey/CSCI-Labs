# Matt Boughey
# CSCI 102 B
# Assessment 07
# References: None
# Time: 45 minutes


list1 = []
list2 = []
rows = int(input("How many rows does the checkerboard have?\nROWS> "))
columns = int(input("How many colums does the checkerboard have?\nCOLUMNS> "))
print("What are the strings with which to pattern it?")
first = input("FIRST> ")
second = input("SECOND> ")
list1.append(first)
list1.append(second)
list2.append(second)
list2.append(first)
print(f"The checkerboard with {rows} rows, {columns} columns, first string is {first}, and second string is {second} is:")
counter = 2

while counter != columns:
    if rows == 1:
        print(f"OUTPUT ['{first}']")
        count3 = 1
        
        break
    list1.append(first)
    counter = counter + 1
    if counter != columns:
        list1.append(second)
        counter = counter + 1
    
counter2 = 2
while counter2 != columns:
    if columns == 1:
        count3 = 1
        
        break
    list2.append(second)
    counter2 = counter2 + 1
    if counter2 != columns:
        list2.append(first)
        counter2 = counter2 + 1
count3 = 0
list3 = []

while count3 != rows:
    if rows == 1:
        #print("['" + first + "']")
        list3.append(first)
        break
    
    print(f"OUTPUT {list1}")
    list3.append(list1)
    count3 = count3 + 1
    if count3 != rows:
        print(f"OUTPUT {list2}")
        list3.append(list2)
        count3 += 1

      
print("And the 2D array representation is:")
print(f"OUTPUT {list3}")
