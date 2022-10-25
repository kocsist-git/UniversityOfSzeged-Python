nev = input("Hogy hívnak? ")    # input adat eltárolása változóban
print("Szia " + nev + "!")

a = input("Első szám: ")         # beolvasás
b = input("Második szám: ")

a = int(a)                       # konvertálás egész számra
b = int(b)

sum = a + b
print("Az összeg: " + str(sum))  # konvertálás stringre
