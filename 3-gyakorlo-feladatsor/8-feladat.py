# 8. feladat: Sorozatok (6 pont)
# Ricsi nagyon szereti a sorozatokat... mármint a matematikai sorozatokat. Kedvencei a számtani és mértani sorozatok. Írj egy sorozat nevű függvényt, amely egy számokból álló listát kap paraméterül! A függvény döntse el, hogy a listában szereplő számok számtani, illetve mértani sorozatot alkotnak-e!

# Kezeld le azt az esetet, amikor a függvény paraméterében érkező lista 3-nál kevesebb elemet tartalmaz! Ekkor a visszatérési érték a HIBA! szöveg legyen! Egyéb hibakezeléssel nem kell foglalkoznod.

# Emlékeztető:
# Egy sorozatot akkor nevezünk számtani sorozatnak, ha a szomszédos elemek különbsége állandó (pl. 1, 3, 5, 7, 9 számtani sorozat, hiszen a szomszédos elemek különbsége mindenhol 2).
# Egy sorozatot akkor nevezünk mértani sorozatnak, ha a szomszédos elemek hányadosa állandó (pl. 1, 2, 4, 8, 16 mértani sorozat, hiszen a szomszédos elemek hányadosa mindenhol 2).
# Példa:
#
# Input: [10, 20]
# Return: 'HIBA!'
#
# Input: [2, 3, 5, 7, 11, 13]
# Return: 'A sorozat se nem szamtani, se nem mertani sorozat.'
#
# Input: [42, 42, 42]
# Return: 'A sorozat szamtani es mertani sorozat is egyben.'
#
# Input: [9, 5, 1, -3, -7]
# Return: 'A sorozat szamtani sorozat.'
#
# Input: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
# Return: 'A sorozat mertani sorozat.'

def sorozat(szamok):
    if len(szamok) < 3: return 'HIBA!'
    kulombseg = szamok[0] - szamok[1]
    szamtani = True
    mertani = True
    for i in range(len(szamok)-1):
        kulombseg2 = szamok[i] - szamok[i+1]
        if kulombseg != kulombseg2: szamtani = False
    
    kulombseg = szamok[1] / szamok[0]
    for i in range(len(szamok)-1):
        kulombseg2 = szamok[i+1] / szamok[i]
        if kulombseg != kulombseg2: mertani = False
    
    if szamtani and not mertani:
        return "A sorozat szamtani sorozat."
    elif mertani and not szamtani:
        return "A sorozat mertani sorozat."
    elif mertani and szamtani:
        return 'A sorozat szamtani es mertani sorozat is egyben.'
    elif not mertani and not szamtani:
        return 'A sorozat se nem szamtani, se nem mertani sorozat.'

print(sorozat([10, 20]))
print(sorozat([2, 3, 5, 7, 11, 13]))
print(sorozat([42, 42, 42]))
print(sorozat([9, 5, 1, -3, -7]))
print(sorozat([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]))
