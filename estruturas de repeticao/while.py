opcao = -1

while opcao != 0:
    opcao = int(
        input("[1] Sacar \n[2] Extrato \n[3] Informações sigilosas \n[0] Sair \n"))

    if opcao == 1:
        print("Sacando")
    elif opcao == 2:
        print("Exibindo extrato")
    elif opcao == 3:
        print("Não era pra você estar aqui.")
        print("Fechando programa..")
        break
        # o break para, corta o loop (funciona no while e no for)
else:
    print("Obrigado paizao")
