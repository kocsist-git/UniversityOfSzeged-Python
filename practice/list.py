### Lista ###

from audioop import reverse
from typing import List


lista = list()
lista2 = []
lista3 = ["gitár", "dob", "mikrofon", "basszusgitar"]

print(len(lista3))

print(lista3[-1])  # utolós elem
print(lista3[2:4])  # 2. elemtől a 4. elemig (4 már nincs benne)
print(lista3[::])  # mindent kiír
print(lista3[:])  # mindent kiír
print(lista3[::-1])  # mindent visszafele
print(lista3[:1:-1])  # 0. és 1. elem kivételével mindent visszaad visszafelé.

for hangszer in lista3:
    print("Egy hangszerfajta a:", hangszer)

print(sorted(lista3))  # lexikografikus rendezés
print(sorted(lista3, reverse=True))  # fordított lexikografikus rendezés
# listává alakítunk egy megfordított listát tartalmazó objektumot
print(list(reversed(lista3)))
print(min(lista3))
print(max(lista3))

lista3.append("cintányér")  # beletesz egy elemet a listába

print(lista3.index("dob"))  # visszatér a dob indexével.

print("cintányér" in lista3)  # True ha bennevan, False ha nincs

lista4 = lista3  # referenciakénti átadás.
lista4 = lista3[:]  # Értékszerinti átadás.

lista3.remove("dob") # törli az alső előfordulást
lista3.count("gitár") # mágszámolja a gitárok számát

Lista5 = lista3 + lista4 # listák összefűzése

lista3.extend(lista4) # a lista3 elemeit kibővíti a lista4 elemeivel

lista4.clear() # kiüríti a listát
del lista4 [:] # kiüríti a listát
del lista4 [:2] # csak a megadott rangeen belüli elemeket törli

lista3.sort() # az eredeti listában módosít, nem add vissza másik listát. 

lista5 = lista3 * 2 # lista sokszorozása
