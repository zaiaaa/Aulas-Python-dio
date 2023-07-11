curso = "pYtHon"

print(curso.upper())

print(curso.lower())

print(curso.title())

texto = "  pawg d   "

# remove todos os espaçoes em branco das bordas
print(texto.strip())
# remove só na esquerda
print(texto.lstrip())
# remove só na direita
print(texto.rstrip())


texto2 = "Python"

# Deixa o texto no meio
print(texto2.center(16, '#'))

print(".".join(texto2))

for i in texto2:
    print(i, end="-")