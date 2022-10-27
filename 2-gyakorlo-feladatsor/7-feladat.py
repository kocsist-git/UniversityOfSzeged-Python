# 7. feladat: Magánhangzó eltávolítás (3 pont)
# Csabi a szabadidejében sokat posztol Twitteren, viszont a posztok hosszúságára 
# vonatkozó 280-as karakterlimitbe gyakran nem fér bele. Egyik nap kitalálta, 
# hogy ha a posztjaiból elhagyja a magánhangzókat, akkor már kevésbé gyűlik meg a
# baja a karakterlimittel.

# Írj egy maganhangzot_torol nevű függvényt, amely egy szöveget vár paraméterül! 
# A függvény távolítsa el a szövegben található összes magánhangzót, 
# majd térjen vissza a magánhangzók nélküli szöveggel!
# A paraméterül kapott szövegben ékezetes betűk garantáltan nem szerepelnek.

# Példa:

# Input: 'Iden Java szigeten voltunk nyaralni. Nem is tudtam, hogy elneveztek egy helyet egy programozasi nyelvrol.'
# Return: 'dn Jv szgtn vltnk nyrln. Nm s tdtm, hgy lnvztk gy hlyt gy prgrmzs nylvrl.'

def maganhangzot_torol(szoveg):
    vissza=""
    for betu in szoveg:
        if betu not in "euioaEUIOA":
            vissza+=betu
    return vissza

print(maganhangzot_torol("Iden Java szigeten voltunk nyaralni. Nem is tudtam, hogy elneveztek egy helyet egy programozasi nyelvrol."))
