# 16. feladat: Gondoltam egy számra (6 pont)
# Készíts egy egyszerű számkitalálós játékot Python nyelven!
# A gép "gondol" egy számra 1 és 1000 között
# (az 1 és az 1000 is még beletartozik a lehetséges számok intervallumába),
# és a felhasználó ezt a számot próbálja meg minél kevesebb próbálkozással kitalálni. 
# A felhasználónak a játék elején 20 élete (próbálkozása) van.

# Hozz létre egy változót a felhasználó életeinek számára! Ennek értéke kezdetben legyen 20!
# Hozz létre egy változót a gondolt számnak! Ez lehet fix szám vagy véletlenszerűen generált érték.
# A játék során minden körben olvasd be a felhasználó aktuális tippjét a konzolról (egész szám)!
# Ha a felhasználó nem találja el a gondolt számot, akkor írasd ki, hogy a gondolt szám kisebb-e vagy
# nagyobb-e a felhasználó tippjénél! Csökkentsd a felhasználó életeinek számát 1-gyel!
# Ha a felhasználó eltalálja a gondolt számot, akkor a játéknak vége, és a felhasználó nyert. 
# Ebben az esetben írasd ki a Gratulalok, nyertel! szöveget, a gondolt számot és a megmaradt életek számát!
# Ha elfogynak a felhasználó életei, akkor a játéknak vége, és a felhasználó veszít. 
# Ebben az esetben írasd ki a Sajnos nem nyertel! szöveget és a gondolt számot!
# 
# Példa:

# Gondoltam egy szamra 1 es 1000 kozott, talald ki, hogy melyikre! Eletek szama: 20
# Tipp: 500
# Kisebb
# Tipp: 250
# Nagyobb
# Tipp: 350
# Nagyobb
# Tipp: 400
# Nagyobb
# Tipp: 450
# Kisebb
# Tipp: 420
# --------------------------------
# Gratulalok, nyertel!
# A gondolt szam valoban 420 volt.
# Megmaradt eletek: 15

import random

elet = 20
gondolt_szam = random.randint(1,1000)
print(f"Gondoltam egy szamra 1 es 1000 kozott, talald ki, hogy melyikre! Eletek szama: {elet}")
while True:
    tipp = int(input("Tipp: "))
    if tipp != gondolt_szam:
        if elet > 1: 
            elet -= 1
            print("Nagyobb" if gondolt_szam > tipp else "Kisebb")
        else:
            print("Sajnos nem nyertel!")
            break
    else:
        print("Gratulalok, nyertel!")
        print(f"A gondolt szam valoban {gondolt_szam} volt.")
        print(f"Megmaradt eletek: {elet}")
        break