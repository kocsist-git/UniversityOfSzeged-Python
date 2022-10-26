# 8. feladat: Gyakorlati jegy (3 pont)
# A Szkriptnyelvek gyakorlat osztályozása a következő ponthatárok alapján történik:

# Ponthatárok	Érdemjegy
# 89 - 100 pont	Jeles (5)
# 76 - 88 pont	Jó (4)
# 63 - 75 pont	Közepes (3)
# 50 - 62 pont	Elégséges (2)
# 0 - 49 pont	Elégtelen (1)
# Írj Python szkriptet, amely beolvassa egy hallgató gyakorlaton elért 
# pontszámát (egész szám), és kiírja a pontszámnak megfelelő érdemjegyet!
# Amennyiben a pontszám 0-nál kisebb vagy 100-nál nagyobb, írasd ki az Ervenytelen ertek!
# hibaüzenetet a konzolra! (Eltekintünk a gyakorlaton szerezhető plusz pontoktól.)

# Példa:

# A pontszamod: 89
# Az erdemjegyed: Jeles (5).
# A pontszamod: -1
# Ervenytelen ertek!

pont = int(input("A potszamod: "))

if pont >= 89:
    print("Jeles (5)")
elif pont >= 76 and pont <= 88:
    print("Jó (4)")
elif pont >= 63 and pont <= 75:
    print("Közepes (3)")
elif pont >=50 and pont <= 62:
    print("Elégséges (2)")
elif pont >=0 and pont <=49:
    print("Elégtelen (1)")
else:
    print("Ervenytelen ertek!") 