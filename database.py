import os

dados = {
    'nome': [],
    'email': [],
    'telefone': [],
    'cpf': []  
}

def limpar_tela():
    os.system('cls')

def inicio():
    print('Bem vindo ao sistema de gerenciamento de dados')
    print()
    print('O que deseja fazer?')
    print('1 - Iniciar o sistema')
    print('2 - Sair do sistema')
    opcao = int(input('Digite a opção desejada: '))
    limpar_tela()
    if opcao == 1:
        print('O sistema foi iniciado com sucesso')
        return True
    elif opcao == 2:
        return False

def fucoes():
    print('Sistema iniciado com sucesso')
    print('1 - Inserir dados')
    print('2 - Exibir dados')
    print('3 - Sair do sistema')
    opcao = int(input('Digite a opção desejada: '))
    limpar_tela()
    if opcao == 1:
        return sistema()
    elif opcao == 2:
        return exibir_dados()
    elif opcao == 3:
        print('Saindo do sistema...')
        return False
       
def sistema():
    print('Insira os dados do cliente')

    nome = input('Nome: ').strip()
    email = input('Email: ').strip()
    telefone = input('Telefone: ').strip()
    cpf = input('CPF: ').strip()

    if not nome or not email or not telefone or not cpf:
        print("Todos os campos são obrigatórios. Cadastro cancelado.")
        return continuar()

    dados["nome"].append(nome)
    dados["email"].append(email)
    dados["telefone"].append(telefone)
    dados["cpf"].append(cpf)

    limpar_tela()
    print(f'Cliente {nome} cadastrado com sucesso')
    return continuar()

def continuar():
    print('O que deseja fazer agora?')
    print('1 - Cadastrar outro cliente')
    print('2 - Exibir dados')
    print('3 - Sair do sistema')

    try:
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:
            limpar_tela()
            return sistema()
        elif opcao == 2:
            limpar_tela()
            return exibir_dados()
        elif opcao == 3:
            limpar_tela()
            print('Saindo do sistema...')
            return False
        
    except ValueError:
        limpar_tela()
        print('Opção inválida. Digite um número válido.')
        return continuar()

def exibir_dados():

    opcao = input('Deseja verifica um ou todos os clientes? (1 - um, 2 - todos): ')
    if opcao == '1':
        if len(dados['nome']) == 0:
            print('Não há clientes cadastrados')
            return continuar()
        
        else:
            nome = input('Digite o nome do cliente que deseja exibir: ')
            if nome in dados['nome']:
                i = dados['nome'].index(nome)
                print(f"{dados['nome'][i]:<15} | {dados['email'][i]:<25} | {dados['telefone'][i]:<15} | {dados['cpf'][i]:<14}")
                print()
                return continuar()
            
            else:
                limpar_tela()
                print('Cliente não encontrado')
                print()
                return continuar()
            
    if opcao == '2':
        if len(dados['nome']) > 0:
            print(f"{'Nome':<15} | {'Email':<25} | {'Telefone':<15} | {'CPF':<14}")
            print('-' * 75)
            for i in range(len(dados['nome'])):
                print(f"{dados['nome'][i]:<15} | {dados['email'][i]:<25} | {dados['telefone'][i]:<15} | {dados['cpf'][i]:<14}")
                print()
        else:
            print('Não há clientes cadastrados')
        return continuar()

if inicio() == True:
    fucoes() 
else:
    print('Saindo do sistema...')