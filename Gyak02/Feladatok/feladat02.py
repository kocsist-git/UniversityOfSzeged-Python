# Készíts egy szorzotabla nevű függvényt, ami kiírja a szorzótáblát 1-től 10-ig!
def szorzotabla():
    line = ""
    for i in range(1, 11):
        for j in range(1, 11):
            line += str(i*j) + " "
        print(line)
        line = ""

szorzotabla()