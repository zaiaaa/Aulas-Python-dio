linguagens = ["python", "java", "c", "java", "csharp"]

# retorna o indice só do primeiro registro encontrado de tal palavra
print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

linguagens2 = ["python", "js", "c", "java", "csharp"]

# remove o ultimo item da lista (ou do index que você por dentro do parametro)
print(linguagens2.pop())  # csharp
print(linguagens2.pop())  # java
print(linguagens2.pop())  # c
print(linguagens2.pop(0))  # python

# Remove apenas o primeiro item que tem "c" como valor
linguagens2.remove("c")
print(linguagens2)  # ["python", "js", "java", "csharp"]

linguagens2.reverse()
print(linguagens2)  # ["csharp", "java", "c", "js", "python"]


# ordena por ordem alfabética como padrão
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

# deixa em ordem alfabética reversa
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

# ordena por tamanho de string
linguagens = ["python", "js", "c", "java", "csharp"]
# ["c", "js", "java", "python", "csharp"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)

# ordena por tamanho de string decrescente
linguagens = ["python", "js", "c", "java", "csharp"]
# ["python", "csharp", "java", "js", "c"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)


linguagens3 = ["python", "js", "c", "java", "csharp"]
# retorna o tamanho da lista
print(len(linguagens3))  # 5

# Faz a mesma coisa do sort
print(sorted(linguagens3, key=lambda x: len(x)))
# ["c", "js", "java", "python", "csharp"]

print(sorted(linguagens3, key=lambda x: len(x), reverse=True))
# ["python", "csharp", "java", "js", "c"]
