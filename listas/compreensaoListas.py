# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]

# Forma 1 de se fazer um filtro em lista
impares = []
for numero in numeros:
    if numero % 2 == 1:
        impares.append(numero)
print(impares)

# forma 2 de se fazer um filtro em lista
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)
