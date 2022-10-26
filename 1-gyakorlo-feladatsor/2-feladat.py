# 2. feladat: Áremelés (3 pont)
# Dávid, a kereskedő számítógép alkatrészeket ad el.
# Mivel mostanság megnőtt a vásárlói igény az alkatrészekre, 
# ezért Dávid úgy dönt, hogy felemeli az árait.

# Írj Python szkriptet, amely beolvassa a standard 
# bemenetről egy adott alkatrész jelenlegi árát (egész szám),
# valamint az áremelés mértékét százalékban (valós szám)! Írasd ki a konzolra, 
# hogy mennyi lesz az alkatrész ára, miután azt az adott százalékkal megnöveljük!
# A végeredményt egész számmá alakítva írasd ki!

# Példa:

# Az alkatresz jelenlegi ara: 17500
# Aremeles (szazalekban): 8.7

# Az alkatresz uj ara: 19022

s1 = input("Az alkatresz jelenlegi ara: ")
s2 = input("Aremeles (szazalekban): ")

print("Az alkatresz uj ara:",int(int(s1)+(int(s1)*(float(s2)/100))))