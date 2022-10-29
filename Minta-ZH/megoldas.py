# 1. Feladat
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
    eredmeny = ""
    for i in range(szamok):
        pass    
    return eredmeny

print (letter_combinations("532"))

class Savanyusag():
    def __init__(self, minoseget_megorzi:tuple, nyitva:bool, elemek, _tipus):
         self.minoseget_megorzi = minoseget_megorzi
         self.nyitva = nyitva
