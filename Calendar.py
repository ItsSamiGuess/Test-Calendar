import calendar
from time import sleep

while True:
    print("")
    calendar.setfirstweekday(calendar.MONDAY)
    yy = 2022
    mm = 1
    print(calendar.month(yy,mm))
    sleep(5)

    while True:        
        monthChange = input("Do you wish to view the next month? (yes/no)  : ")
        if monthChange == ("yes"):
            print("")
            mm +=1
            print(calendar.month(yy,mm))
            sleep(5)
            continue

        if monthChange == ('no'):
            print("Alrightly then.")
            break       
        
        else: 
            sleep(2)
            print("please type 'yes' or 'no'.")
            continue
