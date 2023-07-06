import time as t

opcao = int(input("Informe uma opção:\n [1] Sacar \n [2] Extrato: "))

if opcao is 1:
    valor = float(input("Informe a quantia para o saque: "))
    print(f"Você sacou {valor} Reais.")

elif opcao is 2:
    print("Exibindo extrato...")
    t.sleep(1)

else:
    exit("Opção inválida")


# saldo = 2000.0
# saque = float(input("Informe o valor do saque: "))

# if saldo >= saque:
#     print("Realizando saque!")
# else:
#     print("Saldo Insuficiente!")
