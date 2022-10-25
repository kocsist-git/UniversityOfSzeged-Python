szam = int(input("Adj meg egy számot: "))

if szam < 0:                        # "ha" ág
    print("A beírt szám negatív.")
    print("Abszolútértéke: " + str(abs(szam)) + ".")
elif szam == 0:                     # "egyébként ha" ág
    print("A beírt szám nulla.")
else:                               # "egyébként" ág
    print("A beírt szám pozitív.")

gondolt_szam = input("Gondolj egy számra! Mi az: ")

if not gondolt_szam == 42:                      # logikai "NEM"
    print("A gondolt szám nem 42.")

eletkor = int(input("Hány éves vagy? "))
nem = input("Mi a nemed? (férfi/nő/egyéb) ")

if eletkor >= 18 and nem == "férfi":            # logikai "ÉS"
    print("Nagykorú férfi vagy.")

homerseklet = float(input("Hány fok van odakint? "))

if homerseklet < -20 or homerseklet > 50:       # logikai "VAGY"
    print("Srácok, baj van...")
