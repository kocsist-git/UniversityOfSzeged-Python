# 16. feladat: Győztes (3 pont)
# Természetesen a skribbl.io-s játék végén azt is tudni szeretnénk, hogy ki nyert.
# Írj egy gyoztes nevű függvényt, amely egy pontszám-statisztikát tartalmazó dictionary-t kap
# paraméterül (mint az előző feladatban)! A függvény térjen vissza annak a játékosnak a nevével,
# akinek a legtöbb pontszáma van! Amennyiben több azonos pontszámú játékos van a dictionary-ben,
# akkor a korábban előforduló játékos nevét add vissza!
# 
# Példa:
# 
# Input: {'shronk': 1200, 'Tamas': 1300, 'adam': 1600, 'Wolf': 1700, 'Karoly': 870}
# Return: 'Wolf'

def gyoztes(lista):
    gyoztes = ""
    maxPont=0
    for nev, pont in lista.items():
        if maxPont<pont:
            maxPont=pont
            gyoztes = nev
    
    return gyoztes

print(gyoztes({'shronk': 1200, 'Tamas': 1300, 'adam': 1600, 'Wolf': 1700, 'Karoly': 870}))