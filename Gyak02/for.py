# megszokottol eltero for. listaszeru bejarasra szolgal

for betu in "alma":
    print(betu)

for szam in [12, 23, 34, 45]:
    print(szam)

for i in range(10):             # 0 1 2 ... 7 8 9
    print(i)

for i in range(2, 10):          # 2 3 4 ... 7 8 9
    print(i)

for i in range(1, 100, 3):      # 1 4 7 ... 94 97
    print(i)

for i in range(20, 10, -1):     # 20 19 18 ... 12 11
    print(i)

for i in range(1, 100):
    print(i)

    if i == 42:
        print("Megtaláltuk az élet értelmét!")
        break

print("A legjobb pizzafeltétek:")

for feltet in ["sajt", "bacon", "ananász", "pepperoni"]:
    if feltet == "ananász":
        continue
    print(feltet)
