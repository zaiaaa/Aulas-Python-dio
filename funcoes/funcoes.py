# É igual no JS, a unica diferença é essa opção que temos de já definir um parâmetro

def exibir_mensagem(nome="anônimo"):
    print(f"Olá {nome}")


# Nesse caso, o valor padrão da variável "nome" é 'Anônimo', então se declararmos essa função, sem um parâmetro o valor padrão será exibido
exibir_mensagem()

# Em python conseguimos retornar mais de um valor!


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


# Como está retornando mais de um valor, a função retornará uma tupla.
antecessores = retorna_antecessor_e_sucessor(1)
print(antecessores)

# Percorrendo a tupla gerada pela função
for numeros in antecessores:
    print(numeros)


def calcular_total(numeros):
    return sum(numeros)


# Podemos colocar como parâmetro uma lista também (Dessa eu nao sabia!!)
tudo = calcular_total([10, 20, 34])

print(tudo)


def salvarCarro(marca, modelo, ano, placa):
    # Salva o carro
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# Maneiras de chamar uma função com parâmetros
salvarCarro("Fiat", "Palio", 1999, "ABC-4921")
salvarCarro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-4921")

# * são ARGS, sempre que em alguma operação houver 1 asterisco, a operação receberá uma tupla
# ** são KWARGS, sempre que em alguma operação houver 2 asteriscos, a operação receberá um dicionário
salvarCarro(**{"marca": "Fiat", "modelo": "Palio",
            "ano": 1999, "placa": "ABC-4921"})


udict = {
    1: 'Janeiro',
    2: 'Fevereiro'
}


for meses in udict:
    print(udict[meses])

# O nome do parÂmetro args ou kwargs podem ter qualquer nome, mas é obrigatório ter os asteriscos


def exibirPoema(data_extenso, *args, **kwargs):
    # O .join serve como um + (concatenação)
    texto = '\n'.join(args)
    meta_dados = '\n'.join(
        [f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibirPoema("Sexta-feira, 26 de agosto de 2023", *('tal', 'tal', 'tal'), **
            {"linguagem": "python", "autor": "Tim Peters", "ano": "1999"})


# Objetos de primeira classe

def somar(a, b):
    return a+b


def subtrair(a, b):
    return a-b


def exibirResultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação foi: {resultado}")


# Só passamos o nome da função, sem o ()
exibirResultado(15, 20, somar)
exibirResultado(15, 20, subtrair)


# globalizando variáveis do escopo de uma função

salario = 2000


def salarioBonus(bonus):
    global salario
    salario += bonus
    return salario


print(salarioBonus(500))
