import json
from datetime import datetime

def menu():
    print("1 - Novo Cliente")
    print("2 - Apaga Cliente")
    print("3 - Débito")
    print("4 - Depósito")
    print("5 - Extrato")
    print("6 - Transferência Entre Contas")
    print("7 - Trocar senha")
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
        "conta": conta,
        'extrato': []
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
    tarifa = 0   
    
    if cpf in clientes and clientes[cpf]['senha'] == senha:
        if clientes[cpf]['conta'] == 'plus':
            valor_com_juros = valor * 1.03
            tarifa = valor * 0.03
            taxa = 3
            if (clientes[cpf]['valor'] - valor_com_juros) < -5000.0:
                print(f"Valor solitado maior do que o possivel. Você possui apenas R${clientes[cpf]['valor']},  Tente novamente.")
                return
        else:
            valor_com_juros = valor * 1.05
            tarifa = valor * 0.05 
            taxa = 5
            if (clientes[cpf]['valor'] - valor_com_juros) < -1000.0:
                print(f"Valor solitado maior do que o possivel. Você possui apenas R${clientes[cpf]['valor']},  Tente novamente.")
                return
            
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        saldo_final = clientes[cpf]['valor'] =  clientes[cpf]['valor'] - valor_com_juros
 
        extrato = {
            'data': dt_string,
            'tarifa': f'R$ {tarifa}',
            'saldo': saldo_final,
            'tipo': 'Debito'
        }
        clientes[cpf]['extrato'].append(extrato)

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

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
 
        extrato = {
            'data': dt_string,
            'tarifa': 0,
            'saldo': clientes[cpf]['valor'],
            'tipo': 'Deposito'
        }
        clientes[cpf]['extrato'].append(extrato)

    with open('banco.json', 'w') as f:
        json.dump(clientes, f)
    print(f"Depósito no valor de {valor} realizado!")
    menu()

def extrato():
    with open('banco.json', 'r') as f:
        clientes = json.load(f)
    cpf = input("Digite o CPF: ")
    if cpf not in clientes:
        cpf = input("CPF não encontrado, tente novamente: ")
    senha = input("Digite a senha: ")

    if cpf in clientes and clientes[cpf]['senha'] != senha:
        senha = input("Senha errada, digite novamente: ")
    if cpf in clientes:
        print(f"Nome: {clientes[cpf]['nome']}")
        print(f"CPF: {clientes[cpf]['cpf']}")
        print(f"Tipo de conta: {clientes[cpf]['conta']}")
        for linha in clientes[cpf]['extrato']:
            print(linha)

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
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        
        extrato = {
            'data': dt_string,
            'tarifa': 0,
            'saldo': clientes[cpf]['valor'],
            'tipo': 'Transferência'
        }

        extrato1 = {
            'data': dt_string,
            'tarifa': 0,
            'saldo': clientes[cpf_1]['valor'],
            'tipo': 'Recebimento'
        }

        clientes[cpf]['extrato'].append(extrato)
        clientes[cpf_1]['extrato'].append(extrato1)
        
    with open('banco.json', 'w') as f:
        json.dump(clientes, f)
    menu()

def operacao_livre():
    with open('banco.json', 'r') as f:
        clientes = json.load(f)
    cpf = input("Digite o seu CPF: ")
    if cpf not in clientes:
        cpf = input("CPF não encontrado, tente novamente: ")
    
    senha_nova = input("Digite a sua nova senha: ")
    if cpf in clientes:
        clientes[cpf]['senha'] = senha_nova
    
    with open('banco.json', 'w') as f:
        json.dump(clientes, f)
    
    print("Parabéns, sua senha foi alterada com sucesso!")
    menu()
    

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
