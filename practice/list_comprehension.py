jelszavak = ["1234zd67", "231f", "asd34", "tiedf3324", "$asd$"]

upper_jelszavak = [jelszo.upper() for jelszo in jelszavak]
print(upper_jelszavak)

upper_jelszavak2 = [jelszo.upper() for jelszo in jelszavak if len(jelszo) > 6]
print(upper_jelszavak2)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
hossza = range(len(matrix[0]))
matrix_t = [[sor[i] for sor in matrix] for i in hossza]
print(matrix_t)

szinek = ["piros", "kek", "zold", "sarga"]
dolgok = ["haz", "auto", "fa"]
szines_dolgok = [sz+" "+d for sz in szinek for d in dolgok]
print(szines_dolgok)

lista_a = [1, 2, 3, 4, 6, 7, 8, 9]
lista_b = [2, 3, 4, 5, 8, 9]
lkr = [a for a in lista_a for b in lista_b if a==b]
print(lkr)