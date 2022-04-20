

list1 = []

import csv
file = open("formations.csv", "r")
#reader = csv.reader(file, delimiter = ",")

start = file.read()



with open("formations.csv", "w") as file:
    writer = csv.writer(file, delimiter = ",")
    for i in start:
        list1 = i.split("-")
        print(list1)
        
