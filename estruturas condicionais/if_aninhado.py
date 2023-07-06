CONTA_NORMAL = True
CONTA_UNIVERSITARIA = False
CHEQUE_ESPECIAL = 200

saldo = 500.00
limite = 200

if CONTA_NORMAL or CONTA_UNIVERSITARIA:
    print(f"Bem-vindo ao nosso banco! Você tem {saldo} reais de saldo")
    saque = float(input("Insira quanto você deseja sacar: "))

    if CONTA_NORMAL:
        if saldo >= saque:
            print("Saque realizado com sucesso!")
        elif saque <= (saldo + CHEQUE_ESPECIAL):
            print("Saque realizado com uso do cheque especial!")
        else:
            print(f"Saldo insuficiente! (Saldo atual: {saldo})")
    elif CONTA_UNIVERSITARIA:
        if saldo >= saque:
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente")
else:
    print("Sistema não te reconheceu, entre em contato com seu gerente")
