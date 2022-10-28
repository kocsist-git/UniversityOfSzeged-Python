# 15. feladat: Szöveges végeredmény (3 pont)
# A 14. feladatban szereplő, végeredményeket tartalmazó dictionary tartalmát
# szöveges formátumban is meg szeretnénk jeleníteni. Írj egy szoveges_vegeredmeny nevű függvényt,
# amely egy pontszám-statisztikákat tartalmazó dictionary-t kap paraméterül!
# A függvény járja be a dictionary kulcs-érték párjait, képezzen belőlük {kulcs}: {ertek}
# pont formátumú szövegeket, amiket 1 vesszővel és 1 szóközzel elválasztva fűzzön össze
# (a szöveg végén ne szerepeljen se vessző, se szóköz)! A visszatérési érték az így kapott szöveg.
# 
# Példa:
# 
# Input: {'shronk': 1200, 'Tamas': 1300, 'adam': 1600, 'Wolf': 1700, 'Karoly': 870}
# Return: 'shronk: 1200 pont, Tamas: 1300 pont, adam: 1600 pont, Wolf: 1700 pont, Karoly: 870 pont'

def szoveges_vegeredmeny(lista):
    vegeredmeny = ""
    for nev, ertek in lista.items():
        vegeredmeny+=nev+":"+" "+str(ertek) + " pont, "
    return vegeredmeny[:len(vegeredmeny)-2]

print(szoveges_vegeredmeny({'shronk': 1200, 'Tamas': 1300, 'adam': 1600, 'Wolf': 1700, 'Karoly': 870}))