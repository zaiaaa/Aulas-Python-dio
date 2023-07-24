# os métodos append, count, copy, extend e clear


lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

# faz uma nova lista, copiando tudo o que tem na outra
l2 = lista.copy()
print(l2)

# COUNT
cores = ["azul", "verde", "roxo", "azul"]

# conta quantos elementos (que você pedir) têm na lista
print(cores.count("azul"))
# ------------------------------------------------

# EXTEND
linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

# basicamente você consegue adicionar mais de um item ao mesmo tempo na lista (NÃO RETORNA UMA LISTA DENTRO DA OUTRA)
linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]
# -----------------------------------------------------

lista.clear()
print(lista)
