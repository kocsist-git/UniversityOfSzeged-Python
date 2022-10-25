i = 1

while i <= 10:
    print(i)
    i += 1   # emlékeztető: Pythonban nincs i++

# break: megszakítja az aktuális ismétlést és a szerkezetet követő utasításra ugrik
# continue: megszakítja az aktuális ismétlést és a következő iterációra ugrik

count = 0
while True:         # végtelen ciklust indít
    count += 1

    if count > 5:   # megállási feltétel
        break

    if count == 3:  # a 3-as értéket átugorjuk
        continue

    print(count, "Éljen a Python!")

