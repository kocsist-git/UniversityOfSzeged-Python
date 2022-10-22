class Taska:

    def __init__(self, marka="nincs", szin="fekete", noi=False):
        self.marka = marka
        self.szin = szin
        self.noi = noi
        self.tartalma = list()

    def berak(self, targy):
        self.tartalma.append(targy)
    
    def __str__(self):
        return "Én egy táska vagyok"

en_taskam = Taska()

print(en_taskam)

class Ember:
    def __init__(self, nev, ig_szam):
        self.nev = nev 
        self.ig_szam = ig_szam
    
    def __eq__ (self, masik):
        if not isinstance(masik, Ember):
            return False
        