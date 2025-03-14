saques_realizados = 0
limite_saque = 3
valor_limite_saque = 500
deposito = 0
extrato = ""
saldo = 0


while True:
    print("""
    MENU DE OPERAÇOES:
    [1]Depósito
    [2]Saque
    [3]Extrato
    [0]Sair
        """)
    opcao = int(input("Escolha uma opção:"))

    if opcao == 1:
        valor_depositado = float(input("Digite o valor do depósito:R$"))
        if valor_depositado > 0:
            print("Depósito realizado com sucesso")
            saldo += valor_depositado
            extrato += (f"\nDepósito:R${valor_depositado:.2f}")

        else:
            print("ERRO, Digite um valor válido")

    elif opcao == 2:
        if saques_realizados >= limite_saque:
            print("Desculpe, Limite de saque diário atingido!")
        else:
            valor_saque = float(input("Digite o valor que deseja sacar:R$"))
            if valor_saque < 0:
                print("ERRO, Digite um valor válido")
            elif valor_saque > valor_limite_saque:
                print(f"Desculpe, o valor inserido excede o limite por saque que é de {valor_limite_saque:.2f}")
            elif valor_saque > saldo:
                print("Desculpe, Saldo insuficiente ")
            elif valor_saque <= saldo:
                print("Saque efetuado com sucesso")
                saques_realizados += 1
                saldo -= valor_saque
                extrato += (f"\nSaque:R${valor_saque:.2f}")


    elif opcao == 3:
        if not extrato:
            print("Nenhuma operação realizada")
        else:
            print("=====EXTRATO=====")
            print(extrato)
            print("==================")
            print(f"SALDO:{saldo:.2f}")

    elif opcao == 0:
        print("Saindo....")
        break

    else:
        print("Opçao inválida!Tente novamente ")
