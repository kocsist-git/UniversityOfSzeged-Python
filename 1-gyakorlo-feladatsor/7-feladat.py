# Jónás, a csokigyáros úgy döntött, hogy nyereményjátékot hirdet:
# néhány legyártott csokoládéba egy aranyszelvényt helyez, és a
# szelvények szerencsés megtalálói egy különleges látogatást tehetnek a 
# csokigyárban. Minden csokihoz tartozik egy gyártási sorszám, és Jónás azokba a 
# csokikba tesz aranyszelvényt, amelyek gyártási sorszáma prímszám.

# Írj Python szkriptet, amely beolvassa a konzolról egy csoki gyártási sorszámát (egész szám)! 
# Ha a beolvasott szám prímszám, akkor írasd ki a Gratulalok, nyertel!, 
# ellenkező esetben pedig a Sajnos nem nyert! szöveget a konzolra!

# Emlékeztető: Egy számot akkor nevezünk prímszámnak, ha csak 1-gyel és önmagával osztható.
# Példa:

# Add meg a csoki gyartasi sorszamat: 47
# Gratulalok, nyertel!
# Add meg a csoki gyartasi sorszamat: 49
# Sajnos nem nyert!

num = int(input("Add meg a csoki gyartasi sorszamat: "))

prim = True
for i in range(2,num):
    if num % i == 0 and num != i:
        prim=False
        break
if prim:
    print("Gratulalok, nyertel!")
else:
    print("Sajnos nem nyert!")