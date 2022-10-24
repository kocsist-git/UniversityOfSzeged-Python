halmaz = set()
halmaz3 = {1, 2, 3, 4}

halmaz.add("citrom") # egy elem hozzáadása
halmaz.update(["csoki", "eper"]) # több elem hozzáadása

print(halmaz)

halmaz.remove("csoki")

print(halmaz.pop()) # Viszaad egy véletlen elemet, amit ki is töről

"csoki" in halmaz

halmaz.clear()

# megszamoljuk a különböző betűket

szoveg = "Megszamoljuk a különböző betűk számát"
betuk = set(szoveg)

print(len(betuk))

# megszámoljuk a különböző szavakat

szavak = szoveg.split(" ")
print(len(szavak))
print(szoveg)

# halmaz műveletek

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Unio", A | B)
print("Metszet", A & B)
print("Különbség", A - B)
print("Szimmetrikus kulönbség", A ^ B)