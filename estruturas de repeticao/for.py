texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="\n")
else:
    print("Executa no fim do laço")


# tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")


# O ultimo parâmetro no range é o step.