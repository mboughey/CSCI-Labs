#Matt Boughey
#CSCI102 - B
#Assessment 05A
#References: None
#Time: 15 Minutes

print("Enter Values to add. Enter quit when done.")
total = 0
samples = 0
def main():
    global total
    global samples
    sample = input("Number> ")
    if sample == "quit":
        quit
    else:
        samples = int(samples) + 1
        total = total + int(sample)
        main()
main()
print("The addition of the " + str(samples) + " entered is:")
print("OUTPUT " + str(samples) + " numbers")
print("OUTPUT " + str(total) + " total")
