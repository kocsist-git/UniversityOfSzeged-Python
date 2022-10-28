# 6. feladat: Egyedi szavak száma (5 pont)
# Írj egy egyedi_szavak_szama nevű függvényt, amely egy szöveget kap paraméterül 
# (a szöveg szóközzel elválasztott szavakat tartalmaz)! A függvény adja vissza, hogy hány különböző szó található a szövegben!

# A kis- és nagybetűket ne különböztesd meg (tehát pl. alma és ALMA ugyanaz a szó)!
# A szavak végén lévő pontoktól, felkiáltójelektől, kérdőjelektől és vesszőktől szabadulj
# meg (tehát például Alma? és alma ugyanaz a szó)! Feltehetjük, hogy ezek az írásjelek csak szavak végén fordulnak elő a szövegben.
# Példa:

# Input: 'A macska, vagy mas neven a hazi macska kisebb termetu husevo emlos, amely a macskafelek csaladjaba tartozik.'
# Return: 14

def egyedi_szavak_szama(mondat):
    halmaz = set()
    lista = mondat.split(" ")
    for szo in lista:
        halmaz.add(szo.lower().replace(",",""))
    return len(halmaz)

print(egyedi_szavak_szama('A macska, vagy mas neven a hazi macska kisebb termetu husevo emlos, amely a macskafelek csaladjaba tartozik.'))