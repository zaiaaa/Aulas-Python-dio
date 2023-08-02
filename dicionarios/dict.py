pessoa = {"nome": "Guilherme", "Idade": 28}
# pessoa = dict(nome="Guilherme", idade=28)

print(pessoa)
pessoa["telefone"] = "3333-1234"
print(pessoa)


print(pessoa["nome"])

pessoa["nome"] = "Mafalda"

print(pessoa)


# dict aninhado

contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "1234-5678"},
    "joao@gmail.com": {"nome": "joao", "telefone": "7129-1235"},
    "maria@gmail.com": {"nome": "Maria", "telefone": "9024-1251"},
    "paulo@gmail.com": {"nome": "paulo", "telefone": "9832-6921"},
    "jose@gmail.com": {"nome": "jose", "telefone": "8251-8961", "extra": {"a": 1}}

}

print(contatos["maria@gmail.com"]["telefone"])

extra = contatos["jose@gmail.com"]["extra"]["a"]

print(extra)

for chave in contatos:
    print(chave, contatos[chave])

print('------------')

for chave, valor in contatos.items():
    print(chave, valor)
