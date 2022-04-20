#Matt Boughey
#CSCI101 B
#References: None
#Time: 20 Minutes



    

early = int(input("How many minutes early would you like your alarm to go off?\nEarly> "))
print("What time do you need to get out of bed?")
time1 = int(input("Hours> "))
time2 = int(input("Minutes> "))
newTime = time1 * 60
wakeTime = newTime + time2
alarmTime = (wakeTime - early)



if alarmTime < 0:
       # while alarmTime < 0:
    new = (1440 + alarmTime)
    hours = (new//60)
    minutes = (new%60)
        
                
else:
    hours = (alarmTime//60)
    minutes = (alarmTime%60)
    
while hours < 0:
    hours = hours + 24


hours = str(hours)
minutes = str(minutes)

print("You should set your alarm for:")
print("OUTPUT", (hours.zfill(2)), (minutes.zfill(2)))
