# une os dois conjuntos
conjunto_a1 = {1, 2}
conjunto_b1 = {3, 4}

resultado1 = conjunto_a1.union(conjunto_b1)  # {1, 2, 3, 4}
print(resultado1)

# retorna a intersecção dos conjuntos
conjunto_a2 = {1, 2, 3}
conjunto_b2 = {2, 3, 4}

resultado2 = conjunto_a2.intersection(conjunto_b2)
print(resultado2)  # {2, 3}

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


# pergunta de eles são interligados
conjunto_a6 = {1, 2, 3, 4, 5}
conjunto_b6 = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a6.isdisjoint(conjunto_b6)  # True
print(resultado)

resultado = conjunto_b6.isdisjoint(conjunto_c)  # False
print(resultado)


# {}.add

sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
sorteio.add(42)  # {1, 23, 25, 42}
sorteio.add(25)  # {1, 23, 25, 42}
# Ele não adiciona números que já existem

# {}.copy
sorteio.copy()
# Só copia a lista

# {}.discard
sorteio.discard(1)
# exclui algum valor que você queira excluir, caso você passe algum numero que não exista na lista, não ocorrerá nenhum erro

# {}.pop
sorteio.pop()
# Exclui o primeiro item da lista

# {}.remove
sorteio.remove(0)
# mesma coisa que o discard, mas acontece um erro quando você coloca um valor que não existe

# len
len(sorteio)
# passa o tamanho da lista

# in
1 in sorteio  # true
78912 in sorteio  # false
# pergunta se tal coisa está dentro da lista


# {}.clear
sorteio.clear()
# Só limpa a lista mesmo
