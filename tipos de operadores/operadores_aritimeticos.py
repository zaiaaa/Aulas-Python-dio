produto_1_bruto = 200
produto_2_bruto = 100
# 10% de desconto
desconto = 50

prod_1_aplicado = produto_1_bruto - desconto * produto_1_bruto / 100
prod_2_aplicado = produto_2_bruto - desconto * produto_2_bruto / 100

print(f"{int(prod_1_aplicado)} e {int(prod_2_aplicado)}")


print(produto_1_bruto + produto_2_bruto)
print(produto_1_bruto - produto_2_bruto)
print(produto_1_bruto * produto_2_bruto)
# divisão com resultado decimal
print(produto_1_bruto / produto_2_bruto)
# divisao com resultado inteiro
print(produto_1_bruto // produto_2_bruto)
# potência
print(produto_1_bruto ** produto_2_bruto)
# resto de divisão
print(produto_1_bruto % produto_2_bruto)


x = ((10 ** 2) + 5) * 4
print(x)

y = 10 / 2 + 25 * 2 - 2 ** 2

print(y)
