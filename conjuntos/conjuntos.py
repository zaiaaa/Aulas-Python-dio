# Conjuntos retornam uma lista de objetos NÃO repetidos
# não confie na ordem na ordem de objetos retornados (podem não estar ordenados alfabeticamente ou numericamente)
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}


qlf = ["oio", "oio", "ia"]
a = set(qlf)
print(a)


outraForma = {"python", "java", "python"}
print(outraForma)
