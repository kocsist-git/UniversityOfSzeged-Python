class Szuperhos:
    def __init__(self, nev, szuperero = 50):
        self._nev = nev                  # adattagok létrehozása és inicializálása
        self._szuperero = szuperero
        self.kepessegek = list()
        print("-- Szuperhős létrehozva. --")
    
    @property
    def szuperero(self):
        return self._szuperero
    
    @szuperero.setter
    def szuperero(self, ertek):
        self._szuperero = ertek
    
    @property
    def nev(self):
        return self._nev
    
    @nev.setter
    def nev(self, ertek):
        self._nev = ertek

    def __str__ (self):
        return self._nev + " egy szuperhős, akinek szuperereje " + str(self._szuperero)

     # két szuperhős akkor lesz egyenlő, ha a nevük és a szupererejük megegyezik

    def __eq__(self, masik_hos):
        return self._nev == masik_hos._nev and self._szuperero == masik_hos._szuperero

      # két szuperhős összeadása során a szupererejük összeadódik

    def __add__(self, masik_hos):
        if isinstance(masik_hos, Szuperhos):  # típusellenőrzés
            uj_szuperero = self._szuperero + masik_hos._szuperero
            uj_szuperhos = Szuperhos("Megahős", uj_szuperero)
            return uj_szuperhos
        else:
            print("Egy szuperhőst csak egy másik szuperhőssel lehet összeadni.")
    
    def __iadd__(self, ertek):
        self.kepessegek.append(ertek)
        return self

hos1 = Szuperhos("Thor", 70)
hos1.szuperero = 100
print(hos1.szuperero)
hos1.nev = "Thor2"
print(hos1.nev)
print(hos1)

hos2 = Szuperhos("Hulk", 80)
hos3 = Szuperhos("Hulk", 80)
hos4 = hos1 + hos2
print(hos2 == hos3)
print(hos4) 
hos1+="Telekinezis"
print(hos1.kepessegek)

# __eq__ (egyenlőség)	obj1 == obj2
# __ne__ (nem egyenlőség)	obj1 != obj2
# __add__ (összeadás)	obj1 + obj2
# __sub__ (kivonás)	obj1 - obj2
# __iadd__ (megnövelés)	obj1 += obj2
# __isub__ (csökkentés)	obj1 -= obj2
# __lt__ (kisebb, mint)	obj1 < obj2
# __gt__ (nagyobb, mint)	obj1 > obj2
# __le__ (kisebb vagy egyenlő)	obj1 <= obj2
# __ge__ (nagyobb vagy egyenlő)	obj1 >= obj2

