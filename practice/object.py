class Osztaly:
    pass


class Taska:

    def __init__(self, marka="nincs", szin="fekete", noi=False):
        self.marka = marka
        self.szin = szin
        self.noi = noi
        self.tartalma = list()

    def berak(self, targy):
        self.tartalma.append(targy)

    def keres(self, mit):
        if self.noi:
            print("Ez egy noi taska, nem tudni mi van benne")
            return None
        elif mit in self.tartalma:
            print("Megtaláltam a keresett tárgyat")
            return self.tartalma.pop(self.tartalma.index(mit))
        else:
            print("Nem találtam a tárgyat")
            return None

    def info(self):
        print("Ez egy táska")


en_taskam = Taska()
en_taskam.berak("kulcs")
en_taskam.berak("toll")
en_taskam.berak("fuzet")
en_taskam.keres("kulcs")

noi_taska = Taska("Samsonite", "rozsszin", True)
noi_taska.berak("kulcs")
noi_taska.berak("alma")
noi_taska.berak("konyv")
noi_taska.keres("kulcs")

###
# Dinamikusan hozzáadható új adattag

en_taskam.ar = 30000

print("A táska ára:", en_taskam.ar)

###
# Dinamikusan felulirhato egy fuggveny

def kamu_berak(targ):
    print("Kamu berak lefutott")

en_taskam.berak = kamu_berak
en_taskam.berak("alma")

# Úgy módosítjuk az objektum példányt ahogy szeretnenk, bar ez nem szep megoldas.

# Lathatosag nem letezik
# _nev alahozas karakter jelolessel lehet jelezni, hogy nem publikus hasznalatra szant
# __nev osztalyon kivul elerhetetlen valtozo, de ez sem jelent garanciat. Megkerulheto
# __nev__ Python speciális fuggvenyek
# str_ beepitett nevelfedes feloldasa

