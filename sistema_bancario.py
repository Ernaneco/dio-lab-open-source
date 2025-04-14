menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Informe a opção desejada: 

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = (str(input(menu))).lower()

    if opcao == "d":
        deposito = float(input("Informe o valor do depósito: "))
        if deposito <= 0:
            print("Informe um valor de depósito positivo.")
        else:
            saldo += deposito
            extrato += f"Deposito: {deposito:.2f}\n"

    elif opcao == "s":
        saque = float(input("Informe o valor do saque: "))
        if numero_saques >= LIMITE_SAQUES:
            print("Você excedeu seu limite de saques diários.")
        elif saque <= 0:
            print("Operação falhou, digite um valor válido!")
        elif saque > limite:
            print("Operação falhou, o saque é maior do que o limite permitido por operação.")
        elif saque > saldo:
            print("O saque é maior do que o saldo, digite um valor válido.")
        else:
            saldo -= saque
            extrato += f"Saque: {saque:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        print("\n$$$$$$$$$$$$ EXTRATO $$$$$$$$$$$$\n")
        if extrato == "":
            print("Não foram realizadas movimentações.\n")
        else:
            saldo_final = f"Saldo: {saldo:.2f}\n"
            print(extrato)
            print(saldo_final)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")

print("Operação finalizada, obrigado por usar nosso sistema!")