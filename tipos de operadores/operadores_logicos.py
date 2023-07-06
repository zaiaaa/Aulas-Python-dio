saldo = 1000
saque = 200
limite = 100
conta_especial = True

cliente_normal = saldo >= saque and saque <= limite
# is_able_to_cash_out = saldo >= saque or saque <= limite
print(cliente_normal)

# o not inverte o valor false ou true. (a linha abaixo retorna true)
print(not 1100 > 1500)

cliente_espec = (saldo >= saque and saque <= limite) or (
    conta_especial and saldo >= saque)

print(cliente_espec)