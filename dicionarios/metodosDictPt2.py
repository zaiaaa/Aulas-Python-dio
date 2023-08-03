contato = {"guilherme@gmail.com": {"nome": "guilherme", "telefone": "1234-5678"}}
contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "1234-5678"},
    "joao@gmail.com": {"nome": "joao", "telefone": "7129-1235"},
    "maria@gmail.com": {"nome": "Maria", "telefone": "9024-1251"},
    "paulo@gmail.com": {"nome": "paulo", "telefone": "9832-6921"},
    "jose@gmail.com": {"nome": "jose", "telefone": "8251-8961", "extra": {"a": 1}}
}
# ele adiciona um valor, caso ele NÃO exista
contato.setdefault("CEP", "12350-120")
# Ele não vai substituir o nome, pois ele existe
contato.setdefault("nome", "Silvio")
print(contato)

# ele altera valores do dict
# e também pode adicionar novas chaves e valores
contatos.update(
    {"guilherme@gmail.com": {"nome": "Gui", "telefone": "8765-4321"}})

contatos.update(
    {"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "8125-4611"}})
print(contatos)

# Retorna todos os valores
contatos.values()

# Retorna se está ou não dentro do dict (true ou false)
resultado = "guilherme@gmail.com" in contatos
resultado = "idade" in contatos["guilherme@gmail.com"]

# remove registros
# esse remove tudo
del contatos["guilherme@gmail.com"]
# Esse remove só o nome, o resto continua
del contatos["joao@gmail.com"]["nome"]
