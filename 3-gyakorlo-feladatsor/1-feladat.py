# 1. feladat: Könyvespolc (2 pont)
# Tünde szeret olvasni, így a polcán is sok könyv van. Egyik nap Tünde rendet rak a lakásában, és a könyveit is rendezi.
# Írj egy konyveket_rendez nevű függvényt, amely egy könyvcímekből álló listát kap paraméterül!
# A függvény rendezze a könyvek címét Z-től A-ig (tehát először rendezze a listaelemeket ábécé sorrendbe, majd fordítsa meg a rendezett listát)!
# A visszatérési érték az eredményül kapott lista.

# Példa:

# Input: ['Vajak I', 'Allatfarm', 'Harry Potter es a bolcsek kove', 'A hobbit', 'Szamitogep Architekturak']
# Return: ['Vajak I', 'Szamitogep Architekturak', 'Harry Potter es a bolcsek kove', 'Allatfarm', 'A hobbit']

def konyveket_rendez(lista):
    return sorted(lista, reverse=True)

lista=['Vajak I', 'Allatfarm', 'Harry Potter es a bolcsek kove', 'A hobbit', 'Szamitogep Architekturak']
print(konyveket_rendez(lista))