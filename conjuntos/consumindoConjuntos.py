numeros = {1, 2, 3, 2}
numeros = list(numeros)
print(numeros[1])
print(numeros[0:])

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
