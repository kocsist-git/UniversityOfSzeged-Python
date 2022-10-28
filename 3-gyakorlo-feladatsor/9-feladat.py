# 9. feladat: Gyorsétterem (4 pont)
# A kedvenc gyorséttermünkben a vásárlók belépés után sorszámot húznak, 
# amely alapján leadhatják a rendelésüket. Az étteremben két kassza üzemel: 
# egyiknél a páros, másiknál pedig a páratlan sorszámú rendeléseket szolgálják ki.

# Írj egy kasszahoz_rendel nevű függvényt, amely egy olyan szöveget kap paraméterül, 
# amely pontosvesszővel elválasztott (egész) számokat tartalmaz! 
# A függvény visszatérési értéke egy 2-dimenziós lista, amely 2 részlistából áll: az első részlistába a páros, 
# a második részlistába pedig a páratlan sorszámok kerülnek növekvő sorrendben.

# Példa:

# Input: '42;38;45;40;41;39;44;43;46'
# Return: [[38, 40, 42, 44, 46], [39, 41, 43, 45]]

# Input: '12;16;14'
# Return: [[12, 14, 16], []]

def kasszahoz_rendel(szamok):
    szamLista = szamok.split(";")
    paros=list()
    paratlan=list()
    for szam in szamLista:
        if int(szam) % 2 == 0:
            paros.append(szam)
        else:
            paratlan.append(szam)
    
    dubla = list()
    if len(paros)>0: dubla.append(sorted(paros))
    if len(paratlan)>0:dubla.append(sorted(paratlan))
    return dubla

print(kasszahoz_rendel('42;38;45;40;41;39;44;43;46'))
print(kasszahoz_rendel('12;16;14'))
