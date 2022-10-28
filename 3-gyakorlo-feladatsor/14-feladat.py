# 14. feladat: Végeredmény (5 pont)
# Egy baráti társaság a népszerű skribbl.io játékkal játszik. A játék minden körében egy
# játékos lerajzol egy előre megadott dolgot, amit a többiek megpróbálnak kitalálni.
# Az egyes körök során a játékosok pontokat gyűjtenek.
#
# Írj egy vegeredmeny nevű függvényt, amely egy dictionary-kből álló listát kap paraméterül!
# A dictionary-k az egyes körök eredményeit tartalmazzák: a kulcsok a játékosok nevei,
# az értékek pedig az adott körben a játékos által elért pontszám. 
# A függvény összesítse játékosonként a pontokat, és az így kapott 
# összesítést adja vissza egy dictionary-ben, a példában látható formátumban!
#
# Példa:
#
# Input:
# [
#   { 'shronk': 400, 'Tamas': 200, 'adam': 800, 'Wolf': 500, 'Karoly': 70 },
#   { 'Tamas': 0, 'Wolf': 0, 'Karoly': 200, 'shronk': 0, 'adam': 100 },
#   { 'Wolf': 600, 'adam': 400, 'Karoly': 500, 'shronk': 200, 'Tamas': 300 },
#   { 'Tamas': 500, 'Wolf': 100, 'Karoly': 0, 'shronk': 600, 'adam': 200 },
#   { 'adam': 100, 'Wolf': 500, 'shronk': 0, 'Tamas': 300, 'Karoly': 100 }
# ]
#
# Return: {'shronk': 1200, 'Tamas': 1300, 'adam': 1600, 'Wolf': 1700, 'Karoly': 870}

def vegeredmeny(eredmenyek):
    vegeredmeny = dict()
    for eredmeny in eredmenyek:
        for nev, eredmeny in eredmeny.items():
            if nev in vegeredmeny:
                vegeredmeny[nev] += eredmeny
            else:
                vegeredmeny[nev] = eredmeny
    return vegeredmeny

print(vegeredmeny([
   { 'shronk': 400, 'Tamas': 200, 'adam': 800, 'Wolf': 500, 'Karoly': 70 },
   { 'Tamas': 0, 'Wolf': 0, 'Karoly': 200, 'shronk': 0, 'adam': 100 },
   { 'Wolf': 600, 'adam': 400, 'Karoly': 500, 'shronk': 200, 'Tamas': 300 },
   { 'Tamas': 500, 'Wolf': 100, 'Karoly': 0, 'shronk': 600, 'adam': 200 },
   { 'adam': 100, 'Wolf': 500, 'shronk': 0, 'Tamas': 300, 'Karoly': 100 }
 ]))