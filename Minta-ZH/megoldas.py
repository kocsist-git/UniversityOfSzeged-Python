# 1. Feladat
from tkinter import E


def is_disarium(szam):
    count = 1
    eredmeny = 0
    for szam_jegy in str(szam):
        eredmeny += int(szam_jegy) ** count
        count += 1
    return True if eredmeny== szam else False

print(is_disarium(175))
print(is_disarium(42))

#2. Feladat
def descarte(a,b):
    c = list()
    for betuA in a:
        for betuB in b:
            c.append(betuA + betuB)
    return c

def letter_combinations(szamok):
    szotar = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }

    eredmeny = szotar[szamok[0]]
    for i in range(len(szamok)-1):
        eredmeny = descarte(eredmeny, szotar[szamok[i+1]]) 
    
    return eredmeny

print(letter_combinations("532"))



class Savanyusag():
    def __init__(self, minoseget_megorzi:tuple, nyitva:bool, elemek, _tipus):
         self.minoseget_megorzi = minoseget_megorzi
         self.nyitva = nyitva
