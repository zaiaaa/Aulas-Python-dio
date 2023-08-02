contatos = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "1234-5678"},
    "joao@gmail.com": {"nome": "joao", "telefone": "7129-1235"},
    "maria@gmail.com": {"nome": "Maria", "telefone": "9024-1251"},
    "paulo@gmail.com": {"nome": "paulo", "telefone": "9832-6921"},
    "jose@gmail.com": {"nome": "jose", "telefone": "8251-8961", "extra": {"a": 1}},
    "aw@gmail.com": {"nome": "paulo", "telefone": "9832-6921"},
    "aawwdaw@gmail.com": {"nome": "paulo", "telefone": "9832-6921"}
}
teste = {
    "guilherme@gmail.com": {"nome": "guilherme", "telefone": "1234-5678"},
    "joao@gmail.com": {"nome": "joao", "telefone": "7129-1235"}
}

# Cria chaves para dict
teste.fromkeys(["CEP", "Rua"], "Vazio")
# print(teste)
# nesse caso não funcionou KKKKKKKKKKKK, mas ele adiciona mesmo

# Pega os dados do dict de uma maneira diferente
print(contatos.get("guilherme@gmail.com", {}))

# mostra as chaves do dict
print(contatos.keys())

# Exclui e exibe na tela o registro da chave que você colocar como parâmetro
# o segundo parâmetro é a resposta padrão, caso o programa não encontre o registro que vc colocou
contatos.pop("paulo@gmail.com", 'Não encontrou')

# exclui o ultimo item do dict
contatos.popitem()
print(contatos)

copia = contatos.copy()
print(copia["joao@gmail.com"])
# Só copia toda a lista mesmo (cria um outro dicionario, mas identico)


contatos.clear()
# Só limpa toda a lista mesmo
