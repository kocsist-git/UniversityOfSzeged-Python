# 2. feladat: Fibonacci (3 pont)
# Írj egy fibo nevű függvényt, amely egy n nemnegatív egész számot kap paraméterül,
# és visszatér a Fibonacci-sorozat n-edik tagjával! Nagyobb n-értékek esetén iteratív 
# vagy rekurzív megoldást érdemes használni?

# Emlékeztető: A Fibonacci-sorozat 0. eleme 0, 1. eleme 1, 
# a többi elemet pedig mindig az előző két elem összegeként kapjuk meg. 
# A Fibonacci-sorozat első néhány eleme (a nulladik elemtől kezdve): 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 stb.

# Példa:

# Input: 10
# Return: 55

# Input: 42
# Return: 267914296

def fibo(num):
    if num < 2: 
        return num
    elso = 0
    masodik = 1
    for i in range (1,num):
        harmadik = elso + masodik
        elso = masodik
        masodik = harmadik
    return harmadik

print(fibo(200))