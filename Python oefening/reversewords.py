import array
import collections

user = input("Geef een zin in! : ")

def reverseWords(input): 

    woordenarray = []
    inputWoorden = input.split(" ")
    for woord in inputWoorden:
        woordenarray.append(woord)
    for i in reversed(woordenarray):
        print(i, end = " ")
    
      
reverseWords(user)







