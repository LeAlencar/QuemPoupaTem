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
    import json
    
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
    import json
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
    cpf = input("Digite o CPF: ")
    senha = input("Digite a senha: ")
    valor = input("Digite o valor: ")
    print(f"cpf: {cpf}")
    print(f"senha: {senha}")
    print(f"valor: {valor}")
    menu()

def deposito():
    cpf = input("Digite o CPF: ")
    valor = input("Digite o valor: ")
    print(f"cpf: {cpf}")
    print(f"valor: {valor}")
    menu()

def extrato():
    cpf = input("Digite o CPF: ")
    senha = input("Digite a senha: ")
    print(f"cpf: {cpf}")
    print(f"senha: {senha}")
    menu()

def transfer():
    cpf = input("Digite o CPF(Origem): ")
    senha = input("Digite a senha: ")
    cpf_1 = input("Digite o CPF(Destino): ")
    valor = input("Digite o valor: ")
    print(f"cpf: {cpf}")
    print(f"senha: {senha}")
    print(f"cpf destino: {cpf_1}")
    print(f"valor: {valor}")
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
