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


for numero in range(100):
    if numero == 12:
        continue
        # o continue ele para onde você quer e continua depois
        # nesse exemplo, ele para no 12, deixa um buraco onde era pra
        # estar o numero 12, e continua sua execução (também funciona no while)
    print(numero, end=", ")
