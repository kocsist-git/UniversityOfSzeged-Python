# Készíts egy piramis nevű függvényt, ami egy számot vár, 
# és alábbi piramist rajzolja ki (mindig az aktuális számig, az még legyen benne a kiíratásban)!

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def piramis(szam):
    for i in range(1,int(szam)+1):
        print((str(i) + " ") * i)

piramis(input("Adj meg egy számot a piramishoz: "))