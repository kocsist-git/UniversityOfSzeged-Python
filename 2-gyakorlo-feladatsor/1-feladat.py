# 1. feladat: Abszolútérték-maximum (2 pont)
# Írj egy abs_max nevű függvényt, amely két egész számot vár paraméterül,
# és visszatér ezek abszolútérték-maximumával! Tehát vesszük mindkét szám abszolútértékét,
# és ezek közül visszaadjuk a nagyobbat.

# Példa:

# Input: 12, -15
# Return: 15

def abs_max(num1, num2):
    return abs(num1) if abs(num1) > abs (num2) else abs(num2)

########
def abs_max(num1, num2):
   return max(abs(num1), abs(num2))

print(abs_max(12,-15))