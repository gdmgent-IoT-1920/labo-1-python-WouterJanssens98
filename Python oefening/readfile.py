f = open("namen.txt", "r")

naamDict = {}


if f.mode == 'r' :
    namen = f.read().splitlines()
    
    for naam in namen:
        if naam not in naamDict:
            naamDict[naam] = 1
        else:
            naamDict[naam] += 1
    for naam in naamDict:
        print(naam, end=': ')
        print(naamDict[naam])