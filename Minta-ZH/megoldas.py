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

print(letter_combinations("234"))



class Savanyusag():
    def __init__(self, minoseget_megorzi:tuple, nyitva:bool, _tipus, *elemek):
        self.minoseget_megorzi = minoseget_megorzi
        self.nyitva = nyitva
        self.elemek=elemek
        if len(elemek) == 1:
            self._tipus = _tipus
        else:
            self._tipus="csalamade"

    @property
    def tipus(self): return self._tipus

    @tipus.setter
    def tipus(self, ertek):
        if ertek in self.elemek:
            self._tipus = ertek
    
    def szavatos(self, ev, honap, nap):
        return True if self.minoseget_megorzi >= (ev, honap, nap) else False

    def fedel_csavar(self):
        if self.nyitva:
            self.nyitva = False
        else:
            self.nyitva = True
    
    def __iadd__(self, savanyusag):
        if isinstance(savanyusag,Savanyusag):
            if savanyusag.nyitva and self.nyitva:
                self.elemek=self.elemek + savanyusag.elemek
                return self
            elif not savanyusag.nyitva:
                raise Exception("A masik savanyusag fedele zarva van!")
            elif self.nyitva == False:
                raise Exception("A savanyusag fedele zarva van!")

    def __str__(self) -> str:
        allapot = "nyitva" if self.nyitva else "zárva"
        return f"Savanyitott {self.tipus}, aminek a fedele {allapot}." 
    
    def __imul__(self, haszor):
        self.elemek = self.elemek * haszor
        return self
    
    def __eq__(self, __o):
        if sorted(self.elemek) != __o.elemek: return False
        if sorted(self.minoseget_megorzi) != __o.minoseget_megorzi: return False
        if sorted(self.nyitva) != __o.nyitva: return False
        if sorted(self._tipus) != __o._tipus: return False

savany1 = Savanyusag((1982,8,23),False,"Titkos", "Paprika" )
savany2 = Savanyusag((1982,8,23),False,"Titkos", "Káposzta", "Bab" )
print(savany1)
print(savany2)
print(savany2.tipus)
savany2.tipus = "Bab"
print(savany2.tipus)
print(savany2.szavatos(2022,10,30))
savany2.fedel_csavar()
savany1.fedel_csavar()
print(savany2)
print(savany2.elemek)
savany2 += savany1
print(savany2.elemek) 
savany2 *= 4
print(savany2.elemek) 
print(savany2 == savany1) 