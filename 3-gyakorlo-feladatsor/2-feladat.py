# 2. feladat: Kiárusítás (3 pont)
# Balázs a zsebpénzéből egy új mikrofont szeretne venni. Szerencséjére a kedvenc webshopja épp kiárusítást tart,
# így minden szórakoztató elektronikai termék akciósan vásárolható meg.

# Írj egy akcios_ar nevű függvényt, amely két paramétert vár: a webshopban található mikrofonok eredeti árát 
# (egész számokat tároló lista) és a leárazás mértékét százalékban (valós szám)! 
# A függvény csökkentse a listában lévő árakat az adott százalékkal, és térjen vissza az így kapott listával! 
# Az árak továbbra is egészek legyenek (ne tizedestörtek)!

# Példa:

# Input: [5000, 12000, 10000, 29000, 47000], 30.0
# Return: [3500, 8400, 7000, 20300, 32900]

def akcios_ar(lista, kedvezmeny):
    for i in range(len(lista)):
        lista[i] = int(lista[i] * ((100-kedvezmeny)/100))
    return lista


print(akcios_ar([5000, 12000, 10000, 29000, 47000], 30.0))