saldo = 500
saque = 700

status = "Sucesso" if saldo > saque else "Falha"
print(f"{status} ao realizar o saque!")
