# 5. feladat: Páros számok összege (3 pont)
# Írj Python szkriptet, amely beolvas a standard bemenetről két egész számot: rendre egy zárt intervallum alsó és felső végpontját! A program írja ki a konzolra az intervallumban található páros számok összegét! A beolvasott alsó és felső végpontok még részei az intervallumnak. Hibakezeléssel nem kell foglalkoznod.

# Példa:

# Az intervallum also vegpontja: 42
# Az intervallum felso vegpontja: 100

# A(z) [42; 100] intervallumba eso paros szamok osszege: 2130

num1 = int(input("Az intervallum also vegpontja: "))
num2 = int(input("Az intervallum felso vegpontja: "))
num3 = 0
for i in range(num1,num2+1):
    if i % 2 == 0:
        num3+=i
print(f"A(z) [{num1}; {num2}] intervallumba eso paros szamok osszege:",num3)