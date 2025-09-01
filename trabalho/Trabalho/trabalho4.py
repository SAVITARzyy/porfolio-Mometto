# Trabalho 4 - Sistema de Cadastro de Funcionários
# Este código é feito por Carlos Daniel Alves Mometto

def cadastrar_funcionario(id): # Function to register a new employee
    nome = input('Digite o nome do funcionário: ')
    setor = input('Digite o setor do funcionário: ')
    salario = float(input('Digite o salário do funcionário: '))
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    return funcionario

def listagem(funcionario):
    print(f"ID: {funcionario['id']}, Nome: {funcionario['nome']}, Setor: {funcionario['setor']}, Salário: R$ {funcionario['salario']:.2f}")

def listar_funcionarios(funcionarios): # Function to list all employees or filter by ID or sector
    while True:
        if not funcionarios:
            print('Nenhum funcionário cadastrado.')
            return
        else:
            print('1. Listar todos os funcionários')
            print('2. Listar funcionários por id')
            print('3. Listar funcionários por setor')
            print('4. Retornar ao menu principal')
            opcao = input('Escolha uma opção: ')
            if opcao == '1':
                for funcionario in funcionarios:
                    listagem(funcionario)
                id = int(input('Digite o ID do funcionário: '))
            elif opcao == '2':
                id = int(input('Digite o ID do funcionário: '))
                for funcionario in funcionarios:
                    if funcionario['id'] == id:
                        listagem(funcionario)
                    break
                else:
                    print('Funcionário não encontrado.')
            elif opcao == '3':
                setor = input('Digite o setor do funcionário: ')
                encontrados = [f for f in funcionarios if f['setor'].lower() == setor.lower()]
                if encontrados:
                    for funcionario in encontrados:
                        listagem(funcionario)
                else:
                    print('Nenhum funcionário encontrado nesse setor.')
            elif opcao == '4':
                return

def remover_funcionario(funcionarios): # Function to remove a specific employee by ID
    if not funcionarios:
        print('Nenhum funcionário cadastrado.')
        return
    id = int(input('Digite o ID do funcionário a ser removido: '))
    for i, funcionario in enumerate(funcionarios):
        if funcionario['id'] == id:
            del funcionarios[i]
            print(f'Funcionário com ID {id} removido com sucesso.')
            return
    
                
list_funcionarios = []
id = 1
while True: # Main menu loop
    print('Hello, Carlos Daniel Alves Mometto!')
    print ('=' * 45)
    print ('1 - Cadastrar funcionário')
    print ('2 - Listar funcionários')
    print ('3 - Remover funcionário')
    print ('4 - Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        funcionario = cadastrar_funcionario(id)
        list_funcionarios.append(funcionario)
        id += 1
    elif opcao == '2':
        listar_funcionarios(list_funcionarios)
    elif opcao == '3':
        remover_funcionario(list_funcionarios)
    elif opcao == '4':
        print('Obrigado por usar o sistema!')
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
        continue