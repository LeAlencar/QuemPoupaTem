import json
def menu():
    print("1 - Novo Cliente")
    print("2 - Apaga Cliente")
    print("3 - Débito")
    print("4 - Depósito")
    print("5 - Extrato")
    print("6 - Transferência Entre Contas")
    print("7 - 'Operação Livre'")
    print("0 - Sair")

def newCustomer():
    with open('banco.json', 'r') as f:
        clientes = json.load(f)

    nome = input('Insira o nome do cliente: ')
    cpf = input('Insira seu CPF(somente números): ')   
    conta = input("Qual será o tipo de conta? (comum / plus) ") 
    inicial = float(input("Qual o valor inicial da conta?(somente números) "))
    senha = input("Digite uma senha segura: ")
   
    cliente = {
        "nome": nome,
        "cpf": cpf,
        "senha": senha,
        "valor": inicial,
        "conta": conta
    }

    clientes[cpf] = cliente
    with open('banco.json', 'w') as f:
        json.dump(clientes, f)
    print("USUÁRIO CRIADO COM SUCESSO!!")
    menu()
    
def deleteCustomer():

    cpf = input("Digite o CPF do usuário que deseja deletar: ")
    with open('banco.json', 'r') as f:
        clientes = json.load(f)
    if cpf in clientes:
        clientes.pop(cpf)
         
    with open('banco.json', 'w') as f:
        json.dump(clientes, f)
    print("Cliente deletado!")
    menu()

def debito():
    with open('banco.json', 'r') as f:
        clientes = json.load(f)
    cpf = input("Digite o CPF: ")
    if cpf not in clientes:
        cpf = input("CPF não encontrado, tente novamente: ")
    senha = input("Digite a senha: ")
    if cpf in clientes and clientes[cpf]['senha'] != senha:
        senha = input("Senha errada, digite novamente: ")
    valor = float(input("Digite o valor a ser retirado: "))
    taxa = 0    
    
    if cpf in clientes and clientes[cpf]['senha'] == senha:
        if clientes[cpf]['conta'] == 'plus':
            valor_com_juros = valor * 1.03
            taxa = 3
            if (clientes[cpf]['valor'] - valor_com_juros) < -5000.0:
                print(f"Valor solitado maior do que o possivel. Você possui apenas R${clientes[cpf]['valor']},  Tente novamente.")
                return
        else:
            valor_com_juros = valor * 1.05
            taxa = 5
            if (clientes[cpf]['valor'] - valor_com_juros) < -1000.0:
                print(f"Valor solitado maior do que o possivel. Você possui apenas R${clientes[cpf]['valor']},  Tente novamente.")
                return

        clientes[cpf]['valor'] -= valor_com_juros
    elif clientes[cpf]['senha'] != senha:
        print("Você digitou a senha errada, tente novamente")
    else:
        print("CPF não encontrado!")

    with open('banco.json', 'w') as f:
        json.dump(clientes, f)
    print(f"Valor de R$ {valor} com taxa de ${taxa}% debitado com sucesso!")     
    menu()

def deposito():
    cpf = input("Digite o CPF: ")
    valor = float(input("Digite o valor: "))
    with open('banco.json', 'r') as f:
        clientes = json.load(f)
    if cpf in clientes:
        clientes[cpf]['valor'] += valor
        print(clientes[cpf])

    with open('banco.json', 'w') as f:
        json.dump(clientes, f)
    print(f"Depósito no valor de {valor} realizado!")
    menu()

def extrato():
    cpf = input("Digite o CPF: ")
    senha = input("Digite a senha: ")
    print(f"cpf: {cpf}")
    print(f"senha: {senha}")
    menu()

def transfer():
    with open('banco.json', 'r') as f:
        clientes = json.load(f)
    cpf = input("Digite o CPF(Origem): ")
    if cpf not in clientes:
        cpf = input("CPF não encontrado, tente novamente: ")
    
    senha = input("Digite a senha: ")
    if cpf in clientes and clientes[cpf]['senha'] != senha:
        senha = input("Senha errada, digite novamente: ")
    cpf_1 = input("Digite o CPF(Destino): ")

    if cpf_1 not in clientes:
        cpf_1 = input("CPF de destino não encontrado, digite novamente: ")

    valor = float(input("Digite o valor: "))
    
    if clientes[cpf]['valor'] < valor:
        print(f"Saldo indisponivel, seu saldo é de {clientes[cpf]['valor']}")
        return
    else:
        clientes[cpf_1]['valor'] += valor
        clientes[cpf]['valor'] -= valor
        
    with open('banco.json', 'w') as f:
        json.dump(clientes, f)
    menu()

def operacao_livre():
    print("operação livre(em breve)")
    

def exit():
    print("Tenha um bom dia e até logo!")
    

menu()

while True:
    option = int(input('Selecione uma opção: '))
    if option == 0:
        exit()
        break
    
    if option == 1:
        newCustomer()
    elif option == 2:
        deleteCustomer()
    elif option == 3:
        debito()
    elif option == 4:
        deposito()
    elif option == 5:
        extrato()
    elif option == 6:
        transfer()
    elif option == 7:
       operacao_livre() 
    else: 
        print('Opção inexistente!')
        menu()
