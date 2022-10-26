# 15. feladat: Menekülés (5 pont)
# Józsi a koronavírus-járvány miatti kijárási korlátozások idején egy házibuliban vesz részt. 
# Sajnos ezt a rendőrök is megtudták, és rajtaütöttek az önfeledten bulizókon,
#  ezért a házibuli résztvevői pánikolva próbálnak elmenekülni a rend éber őrei elől.

# Írj Python szkriptet, amely beolvas két egész számot: rendre a házibuliban résztvevők számát 
# és a rendőrök számát! A rendőrök úgy kapják el a bulizókat, hogy az 
# első rendőr elkap 1 bulizót, majd minden további rendőr 1-gyel többet kap el, 
# mint az előző (tehát az első rendőr 1, a második rendőr 2, 
# a harmadik rendőr 3 bulizót kap el és így tovább).

# Ha senkit nem kaptak el a rendőrök, akkor írasd ki a Minden bulizo megmenekult!
# szöveget a konzolra!
# Ha mindenkit elkaptak a rendőrök, akkor az Ajaj, mindenkit elkaptak! szöveget írasd ki!
# Minden egyéb esetben a következő szöveget jelenítsd meg a konzolon:
# {elkapottak szama} bulizot elkaptak, {elmenekultek szama} pedig elmenekult. 
# (a kapcsos zárójelek helyére értelemszerűen a megfelelő értékek legyenek behelyettesítve)!
# Példa:

# A hazibuliban resztvevok szama: 8
# A rendorok szama: 3

# 6 bulizot elkaptak, 2 pedig elmenekult.
# A hazibuliban resztvevok szama: 20
# A rendorok szama: 6

# Ajaj, mindenkit elkaptak!
# A hazibuliban resztvevok szama: 10
# A rendorok szama: 0

# Minden bulizo megmenekult!

bulizok = int(input("A hazibuliban resztvevok szama: "))
rendorok = int(input("A rendorok szama: "))
act_buli = bulizok
elkap = 0
while True:
    if rendorok > 0:
        elkap+=1
        act_buli -= elkap
        rendorok -= 1
    else:
        break

if act_buli < 0:
    print("Ajaj, mindenkit elkaptak")
elif bulizok == act_buli:
    print("Minden bulizó megmenekült!")
else:
    print(f"{bulizok - act_buli} bulizot elkaptak, {act_buli} pedig elmenekult")
    