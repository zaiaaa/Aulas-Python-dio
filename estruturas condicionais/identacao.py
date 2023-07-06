def Sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado")
        print("Retire o seu dinheiro no caixa")
    else:
        print("Saldo insuficiente")


def Depositar(valor):
    saldo = 500
    saldo += valor

    print(f"Você depositou {valor}. Agora você tem {saldo} de saldo")


print("Obrigado por ser nosso cliente")

Depositar(100)
# Sacar(700)
