# a String immutable

egy_soros_szoveg = "almafa"
egy_soros_szoveg = 'almafa'

tobb_soros_szoveg = """Egy, egy almafa
Kettő, két katica
Három, három kiskacsa
Egy, kettő, három"""

szoveg = "szkript" + "nyelvek"
print(szoveg)   

szoveg = str(101) + " kiskutya" # csak strigeket lehet osszefuzni
print(szoveg)       

szoveg = "Python"
print(len(szoveg)) # hossz lekerdezese

szoveg = "macskajancsi"
print("A 0. indexű karakter:", szoveg[0])   
print("A 4. indexű karakter:", szoveg[4])   

print("Az utolsó karakter:", szoveg[-1]) # negativ index a szoveg vegerol kezdni

print("4-10. karakter, 2-es lépésközzel:", szoveg[4:10:2])  
print("2-5. karakter:", szoveg[2:5])
print("Elejétől a 6. karakterig:", szoveg[:6])
print("6. karaktertől a string végéig:", szoveg[6:])
print("A teljes szöveg:", szoveg[:])
print("Minden második karakter:", szoveg[::2])

print(szoveg[::-1]) # string megforditasa

szoveg = "1, egy almafa; 2, két katica; 3, három kiskacsa; 1, 2, 3"

if "alma" in szoveg:
    print("Van a szövegben alma.")

if szoveg[0] in "0123456789":
    print("A szöveg egy számjeggyel kezdődik.")

# s.lower(): csupa kisbetűssé alakítja az s stringet
# s.upper(): csupa nagybetűssé alakítja az s stringet
# s.startswith(v): igazat ad vissza, ha az s string a v értékkel kezdődik
# s.endswith(v): igazat ad vissza, ha az s string a v értékre végződik
# s.count(v): visszaadja, hogy az s stringben hányszor szerepel a v érték
# s.strip(): eltávolítja az s string elején és végén lévő helyközöket
# s.lstrip(): csak az s string elején lévő helyközöket távolítja el (left strip)
# s.rstrip(): csak az s string végén lévő helyközöket távolítja el (right strip)
# s.replace(old, new): lecseréli az s stringben az összes old részstringet new-ra
# s.split(delim): feldarabolja az s stringet delim karakterek mentén (listát ad vissza)
# s.isalpha(): igazat ad vissza, ha az s stringben csak betűk szerepelnek
# s.isdigit(): igazat ad vissza, ha az s stringben csak számjegyek szerepelnek

szoveg = "   A füstölt szalonna a legjobb szalonna Béla szerint                "
szoveg = szoveg.strip()   # helyközök eltávolítása a szöveg elejéről és végéről

print(szoveg.lower())               # kisbetűsítés
print(szoveg.upper())               # nagybetűsítés
print(szoveg.endswith("szerint"))   # a "szerint" stringre végződik-e a szöveg
print(szoveg.count("a"))            # hány darab 'a' betű van a szövegben
print(szoveg.replace("szalonna", "kolbász"))  # lecserélés
print(szoveg.split(" "))            # feldarabolás szóközök mentén

# formazas 

PI = 3.14159265359
print("A pí értéke: {}".format(PI))                   # format() metódus

nev = "Béla"
eletkor = 21
print("Hello, %s vagyok, %d éves." % (nev, eletkor))  # %-formatting

elet_ertelme = 42
print(f"Az élet értelme: {elet_ertelme}")             # f-string
