# 13. feladat: Heti profit (3 pont)
# A csokigyáros Jónás nyereményjátéka nagy sikert aratott a vásárlók körében. 
# A statisztikák alapján a csokigyár mindennap kétszer annyi csokit ad el, mint az előző napon.
#  Jónás ki szeretné számolni, hogy egy héten várhatóan mennyi csokit fog eladni.

# Írj Python szkriptet, amely beolvassa a hétfőn eladott csokik számát (egész szám),
# majd kiszámítja, hogy 7 nap alatt összesen mennyi csokit fog eladni Jónás, 
# ha mindennap kétszer annyi csokit ad el, mint az előző napon!
# (Tehát pl. ha hétfőn 500 csokit ad el, akkor kedden 1000-et, szerdán 2000-et stb.,
# ezeket az értékeket kell összeadogatni.)

# Példa:

# A hetfon eladott csokik szama: 500
# A heten varhatoan 63500 csokit adunk el.
# A hetfon eladott csokik szama: 2345
# A heten varhatoan 297815 csokit adunk el.

eladott_csokik = int(input("A hetfon eladott csokik szama: "))
osszesen=0
for i in range(7):
    osszesen+=eladott_csokik
    eladott_csokik=eladott_csokik*2

print(f"A heten varhatoan {osszesen} csokit adunk el.")