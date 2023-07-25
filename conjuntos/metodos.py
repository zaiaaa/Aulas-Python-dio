# une os dois conjuntos
conjunto_a1 = {1, 2}
conjunto_b1 = {3, 4}

resultado1 = conjunto_a1.union(conjunto_b1)  # {1, 2, 3, 4}
print(resultado1)

# retorna a intersecção dos conjuntos
conjunto_a2 = {1, 2, 3}
conjunto_b2 = {2, 3, 4}

resultado2 = conjunto_a2.intersection(conjunto_b2)
print(resultado2)

# retorna as diferenças de um conjunto pro outro
conjunto_a3 = {1, 2, 3}
conjunto_b3 = {2, 3, 4}

resultado3 = conjunto_a3.difference(conjunto_b3)
print(resultado3)

resultado4 = conjunto_b3.difference(conjunto_a3)
print(resultado4)

# retorna as diferenças dos dois conjuntos
conjunto_a4 = {1, 2, 3}
conjunto_b4 = {2, 3, 4}

resultado = conjunto_a4.symmetric_difference(conjunto_b4)
print(resultado)

# basicamente pergunta se um conjunto é subconjunto de outro
conjunto_a5 = {1, 2, 3}
conjunto_b5 = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a5.issubset(conjunto_b5)  # True
print(resultado)

resultado = conjunto_b5.issubset(conjunto_a5)  # False
print(resultado)
