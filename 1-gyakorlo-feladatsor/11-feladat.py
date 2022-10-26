# 11. feladat: Számológép (5 pont)
# Pomeló Zoltán egy zöldségesboltot üzemeltet. Ahhoz, hogy az árakat könnyebben tudja számolni,
# szüksége van egy számológépre. Írj Pythonban egy egyszerű számológépet, amely a négy 
# alapműveletet (összeadás, kivonás, szorzás, osztás) tudja értelmezni!

# Olvass be a standard bemenetről két valós számot és egy műveleti jelet (string)!
# Ha a műveleti jel helyes (tehát a +, -, *, / szimbólumok valamelyike), akkor végezd el
# a műveletet és írasd ki az eredményt a konzolra!
# A felsorolt 4 jeltől eltérő műveleti jel esetén írasd ki a Hibas muveleti jel! üzenetet a konzolra!
# Kezeld le a nullával való osztás esetét is: ha nullával szeretnénk osztani,
# akkor írasd ki a konzolra az Ejnye, nullaval nem osztunk! hibaüzenetet!
# 
# Figyelem! A Python a valós számokat nem pontosan ábrázolja, 
# ezért a rajtuk végzett aritmetikai műveletek "különös" eredményeket
# produkálhatnak (pl. 0.1 + 0.2 eredménye 0.30000000000000004). 
# Ennek kiküszöböléséhez kerekítsük 2 tizedesjegyre a kiszámolt eredményt: round(szám, 2) !

#Példa:

# Elso szam: 3.8
# Masodik szam: 4.2
# Muvelet: *
# Az eredmeny: 15.96

# Elso szam: 5.0
# Masodik szam: 0.0
#Muvelet: /

#Ejnye, nullaval nem osztunk!

szam1 = float(input("Elso szam: "))
szam2 = float(input("Masodik szam: "))
muvelet = input("Muvelet: ")
eredmeny=0
if muvelet=="*":
    eredmeny=szam1*szam2
elif muvelet=="/":
    if szam2==0:
        print("Ejnye, nullaval nem osztunk!")
    else:
        eredmeny=szam1/szam2
elif muvelet == "+":
    eredmeny=szam1+szam2
elif muvelet== "-":
    eredmeny = szam1-szam2
else:
    print("Hibas muveleti jel!")

print(f"Az eredmeny: {eredmeny}")