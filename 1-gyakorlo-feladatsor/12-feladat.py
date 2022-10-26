# 12. feladat: Ösztöndíj (4 pont)
# Egy kisváros ösztöndíjat hirdet azoknak az egyetemi hallgatóknak, akiknek a tanulmányi átlaguk legalább négyes. Írj Python szkriptet, amely először beolvassa, hogy hány jegyet kapott az adott egyetemi hallgató a félévben (egész szám), majd ezt követően beolvas ennyi darab érdemjegyet (egész számok)! A szkript számítsa ki a jegyek átlagát, és döntse el, hogy a hallgató jogosult-e az ösztöndíjra vagy sem (tehát legalább 4.0 az átlaga vagy sem)!

# Emlékeztető: Az átlagot a jegyek összegének és darabszámának hányadosaként kapjuk meg.
# Példa:

# Hallgato jegyeinek szama: 5
# A jegyek:
# 3
# 5
# 5
# 4
# 5

# A jegyek atlaga: 4.4
# A hallgato osztondijra jogosult!
# Hallgato jegyeinek szama: 3
# A jegyek:
# 3
# 1
# 5

# A jegyek atlaga: 3.0
# A hallgato nem jogosult osztondijra!

jegyekSzama=int(input("Hallgato jegyeinek szama: "))
jegyek = list()
print("A jegyek: ")
for i in range(jegyekSzama):
    jegyek.append(int(input()))

osszeg=0
for jegy in jegyek:
    osszeg += jegy

atlag = osszeg / len(jegyek)

print(f"A jegyek atlaga: {atlag}")
if atlag >= 4:
    print("A hallgato osztondijra jogosult!")
else:
    print("A hallgato osztondijra nem jogosult!")