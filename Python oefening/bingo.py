import random
from termcolor import colored, cprint

randNumber = random.randrange(1000,9999)

randString = str(randNumber)



inputNumber = input("Geef een 4-cijferig nummer in  :    ")


print("Het random gegenereerde nummer is {0}".format(randString))

kipCount = 0 
eiCount = 0
if inputNumber == randString:
    print("Miljaar wat een prestatie, wat een prestatie....")
else:
    i = 0
    for number in randString:
        if number == inputNumber[i]:
            cprint("Je hebt een kip!", "green")
            kipCount += 1

        elif number in inputNumber:
            cprint("Je hebt een ei", "yellow")
            eiCount += 1

        else:
            cprint("Je hebt niets!", "red")
        i += 1
    
    cprint("Je totale resultaat = {0} x kip & {1} x ei".format(kipCount, eiCount), "blue")