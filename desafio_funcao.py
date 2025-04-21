def cadastrar_usuario(usuarios):

    print("Iniciando cadastro de usuário no sistema\n")

    cpf = str(input("Digite o seu CPF (somente números): "))
    usuario = filtrar_usuarios(cpf, usuarios)

    # Se o usuário já existir, encerrar o cadastro
    if usuario:
        print("Usuário já consta no sistema com o CPF informado!")
        return
      
    nome = str(input("Digite o seu nome: "))
    data_nascimento = str(input("Digite a sua data de nascimento (XX/XX/XXXX): "))
    endereco = str(input("Digite o seu endereço (logradouro - nr - bairro - cidada - sigla estado): "))
    
    usuarios.append({"CPF": cpf, "nome": nome, "data_de_nascimento": data_nascimento, "endereço": endereco})

    print("Usuário cadastrado no sistema com sucesso!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = []
    # Loop para filtrar usuários por CPF
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            usuarios_filtrados = [usuario]

    # Se o filtro encontrar o usuário, retorná-lo
    if usuarios_filtrados:
        return usuarios_filtrados[0]
    else:
        None

def cadastrar_conta(AG, numero_conta, usuarios):
    cpf = input("Digite o seu CPF para abrir a conta: ")
    
    # Buscando o usuário
    usuario = filtrar_usuarios(cpf, usuarios)

    # Se o usuário tiver cadastrado no banco
    if usuario:
        print("Conta criada com sucesso!")
        # Criando o dicionário com as informações da conta
        return {"agência": AG, "número_da_conta": numero_conta, "usuário": usuario}

    # Caso o cliente ainda não tenha cadastro no sistema
    print("Usuário não cadastrado no sistema. Gentileza efetuar o cadastro primeiro.")

def sacar(*, saldo, saque, extrato, limite, numero_saques, LIMITE_SAQUES): # argumentos chamados pelo nome
        
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
        print("Saque realizado com sucesso!")
    return saldo, extrato

def depositar(deposito, saldo, extrato, /): # chamando argumentos por posição
    
    if deposito <= 0:
        print("Informe um valor de depósito positivo.")
    else:
        saldo += deposito
        extrato += f"Deposito: {deposito:.2f}\n"
        print("Depósito realizado com sucesso!")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato): # saldo chamado por posição e extrato pelo nome
    print("\n$$$$$$$$$$$$ EXTRATO $$$$$$$$$$$$\n")
    if extrato == "":
        print("Não foram realizadas movimentações.\n")
    else:
        saldo_final = f"Saldo: {saldo:.2f}\n"
        print(extrato)
        print(saldo_final)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agência']} \nConta: {conta['número_da_conta']} \nCliente: {conta['usuário']['nome']}")

def main():

    menu = """

    [c] Cadastrar usuário
    [a] Abrir conta
    [l] Listar contas
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    Informe a opção desejada: 

    """
    # Variáveis
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    # Constantes
    LIMITE_SAQUES = 3
    AG = "0001"

    while True:

        opcao = (str(input(menu))).lower()

        if opcao == "c":
            cadastrar_usuario(usuarios)
            

        elif opcao == "a":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AG, numero_conta, usuarios)
            
            # Se a conta foi criada, adicionar a lista de contas
            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)


        elif opcao == "d":
            deposito = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(deposito, saldo, extrato)
            

        elif opcao == "s":
            saque = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo, 
                saque=saque, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

main()
print("Operação finalizada, obrigado por usar nosso sistema!")



