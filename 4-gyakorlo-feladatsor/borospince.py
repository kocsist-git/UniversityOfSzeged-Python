# A feladatsor linkje: https://cservz.github.io/teaching/szkriptnyelvek/feladatsorok/04/

class BorospinceException(Exception):
    def __init__(self,hiba):
        super().__init__(hiba)

class Bor():
    def __init__(self, fajta, evjarat, alkoholtartalom=12.5):
        self._fajta = fajta
        self._evjarat = evjarat
        self.alkoholtartalom = alkoholtartalom

    @property
    def fajta(self): return self._fajta

    @fajta.setter
    def fajta(self, fajta): self._fajta = fajta

    @property
    def evjarat(self): return self._evjarat

    @evjarat.setter
    def evjarat(self, evjarat): self._evjarat = evjarat

    @property
    def alkoholtartalom(self): return self._alkoholtartalom

    @alkoholtartalom.setter
    def alkoholtartalom(self, alkoholtartalom):
        if isinstance(alkoholtartalom, float) and 0 <= alkoholtartalom <= 100: 
            self._alkoholtartalom=alkoholtartalom
        else:
            raise BorospinceException("Nem megfelelo alkoholtartalom!")
    
    def __str__(self):
        return f"{self._fajta} (evjarat: {self._evjarat}), melynek alkoholtartalma: {self._alkoholtartalom}%"
    
    def __eq__(self, object):
        if isinstance(object, Bor):
            return self.alkoholtartalom == object.alkoholtartalom and self.evjarat == object.evjarat and self.fajta.lower() == object.fajta.lower()
        else:
            return False

class Szekreny():
    def __init__(self):
        self.borok = list()
    
    def get_bor(self,szam):
        if szam > -1 and szam < len(self.borok):
            return self.borok[szam]
        else:
            raise BorospinceException("Nem letezo index!")
    
    def __iadd__(self, bor):
        if isinstance(bor, Bor):
            self.borok.append(bor)
            return self
        else:
            raise TypeError("Nem bor!")   

    def __add__(self, szekreny):
        if isinstance(szekreny, Szekreny):
            ujSzekreny = Szekreny()
            ujSzekreny.borok=self.borok+szekreny.borok
            return ujSzekreny
    
    def atlag_alkoholtartalom(self):
        if len(self.borok) == 0: return BorospinceException("Ures a szekreny!") 
        ossz_alkohol = 0
        for bor in self.borok:
            ossz_alkohol += bor.alkoholtartalom
        
        return ossz_alkohol / len(self.borok)

    def statisztika(self):
        eredmeny = dict()

        for bor in self.borok:
            
            if bor.fajta.lower() in eredmeny:
                eredmeny[bor.fajta.lower()] += 1
            else:
                eredmeny[bor.fajta.lower()] = 1
        return eredmeny

    def megisszak(self, bor:Bor):
        if bor not in self.borok:
            raise BorospinceException ("Bor nem talalhato!")
        if not isinstance(bor, Bor): 
            raise BorospinceException("Nem bor!")

        self.borok.remove(bor)
         
    def __str__(self):
        if len(self.borok) == 0: return "Ez egy ures szekreny"
        stat = self.statisztika()
        eredmeny = ""
        for nev,darab in stat.items():
            eredmeny += str(darab) + " " + nev + ", "
        return eredmeny[:-2]


bor1 = Bor('Tokaji aszu', 2017, 13.5)
bor2 = Bor('Gyanus kinezetu kannasbor', 2010)
bor3 = Bor('ToKaJi AsZu', 2015, 13.8)
bor4 = Bor('Chardonnay', 2019, 13.0)

bor2.fajta = 'Egri bikaver'
bor2.evjarat = 2013
bor2.alkoholtartalom = 12.0
print(f'{bor2.fajta}, {bor2.evjarat}, {bor2.alkoholtartalom}')  # 'Egri bikaver, 2013, 12.0'

print(bor1)                  # 'Tokaji aszu (evjarat: 2017), melynek alkoholtartalma: 13.5%'
print(bor1 == Bor('TOKAJI ASZU', 2017, 13.5))   # True
print(bor1 == bor2)                             # False
print(bor1 == 'Hibas tipusu parameter!')        # False

szekreny1 = Szekreny()
szekreny2 = Szekreny()

szekreny1 += bor1
szekreny1 += bor2
szekreny1 += bor3
szekreny2 += bor4

szekreny3 = szekreny1 + szekreny2

print(szekreny3.get_bor(0))                   # 'Tokaji aszu (evjarat: 2017), melynek alkoholtartalma: 13.5%'
print(szekreny3.get_bor(3))                   # 'Chardonnay (evjarat: 2019), melynek alkoholtartalma: 13.0%'
print(szekreny3.atlag_alkoholtartalom())      # 13.075

szekreny2.megisszak(bor4)
print(szekreny2.statisztika())                # {}
print(szekreny3.statisztika())                # {'tokaji aszu': 2, 'egri bikaver': 1, 'chardonnay': 1}

print(szekreny2)                              # 'Ez egy ures szekreny.'
print(szekreny3)     