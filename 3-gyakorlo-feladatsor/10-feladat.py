# 10. feladat: Mátrixok összeadása (6 pont)
# Írj egy matrix_osszead nevű függvényt, amely két mátrixot (2-dimenziós listát) vár paraméterül,
# és kiszámítja ezen két mátrix összegét! A feladat megoldása során ne használj semmilyen beépített vagy külső Python csomagot!
#
# Fontos, hogy az összeadásnál mindkét mátrix dimenziószáma megegyezzen
# (pl. mindkét mátrix n x m-es legyen, azaz n sorból és m oszlopból álljon). 
# Ha a két mátrix dimenziószáma eltér, akkor a függvény térjen vissza egy üres listával!
# Ha a dimenziószámok megegyeznek, akkor a visszatérési érték a két mátrix összege legyen (ami szintén egy mátrix)!
#
# Segítség: Két mátrix összegét úgy kapjuk, hogy az azonos indexeken lévő elemeket rendre összeadogatjuk. Például:Mátrix összeadás
# Példa:
#
# Input: [[7, 1, 3], [4, 0, 2]], [[2, 5, 5], [8, 6, 0]]
# Return: [[9, 6, 8], [12, 6, 2]]
#
# Input: [[5, 1], [3, 2], [8, 6]], [[4, 8], [2, 7]]
# Return: []

def matrix_osszead (matrix1, matrix2):
    if len(matrix1) != len(matrix2): return [] 
    eredmeny = [],[]

    for i in range(len(matrix1[0])):
        eredmeny[0].append(matrix1[0][i]+matrix2[0][i])
        eredmeny[1].append(matrix1[1][i]+matrix2[1][i])
    return eredmeny

print(matrix_osszead([[7, 1, 3], [4, 0, 2]], [[2, 5, 5], [8, 6, 0]]))
print(matrix_osszead([[5, 1], [3, 2], [8, 6]], [[4, 8], [2, 7]]))