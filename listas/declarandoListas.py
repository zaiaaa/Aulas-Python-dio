frutas = ["laranja", "maçã", "uva"]
print(frutas)
# maçã
print(frutas[1])

# pega sempre o ultimo elemento (e assim sucessivamente com os numeros negativos)
print(frutas[-1])

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)


matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "C"]
]
print(matriz)

# Retorna o primeiro conjunto de valores
print(matriz[0])

# Retorna o primeiro item do primeiro conjunto
print(matriz[0][0])

# Retorna o último item do primeiro conjunto
print(matriz[0][-1])


# FATIAMENTO
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
# pega e exibe do indice 0 ao 3 com step em 2 (pega de 2 em 2))
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
