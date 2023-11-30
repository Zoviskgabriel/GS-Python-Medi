
# Lista para armazenar informações dos pacientes, suas receitas e estoque
pacientes = {}

# Cadastro de um novo paciente
def cadastrar_usuario(nome):
    if nome not in pacientes:
        pacientes[nome] = {'receitas': [], 'estoque': {}}
        print(f"Paciente '{nome}' cadastrado com sucesso.")
    else:
        print("Paciente já existe.")

# Funcionalidade para adicionar uma receita médica a um paciente
def adicionar_receita(nome, receita):
    if nome in pacientes:
        pacientes[nome]['receitas'].append(receita)
        print(f"Receita médica adicionada para o paciente '{nome}'.")
    else:
        print("Paciente não encontrado.")

# Funcionalidade para adicionar/remover medicamentos ao estoque de um usuário
def gerenciar_estoque_usuario(nome, medicamento, quantidade, adicionar=True):
    if nome in pacientes:
        if adicionar:
            if medicamento in pacientes[nome]['estoque']:
                pacientes[nome]['estoque'][medicamento] += quantidade
            else:
                pacientes[nome]['estoque'][medicamento] = quantidade
            print(f"{quantidade} unidades de {medicamento} adicionadas ao estoque de '{nome}'.")
        else:
            if medicamento in pacientes[nome]['estoque'] and pacientes[nome]['estoque'][medicamento] >= quantidade:
                pacientes[nome]['estoque'][medicamento] -= quantidade
                print(f"{quantidade} unidades de {medicamento} removidas do estoque de '{nome}'.")
            else:
                print("Quantidade insuficiente no estoque.")
    else:
        print("Paciente não encontrado.")

# Funcionalidade para exibir as receitas médicas de um paciente
def exibir_receitas(nome):
    if nome in pacientes:
        print(f"\nReceitas médicas do paciente '{nome}':")
        for receita in pacientes[nome]['receitas']:
            print(receita)
    else:
        print("Paciente não encontrado.")

# Funcionalidade para exibir o estoque de um paciente
def exibir_estoque(nome):
    if nome in pacientes:
        print(f"\nEstoque atual do paciente '{nome}':")
        if pacientes[nome]['estoque']:
            for medicamento, quantidade in pacientes[nome]['estoque'].items():
                print(f"{medicamento}: {quantidade} unidades")
        else:
            print("O estoque está vazio para este paciente.")
    else:
        print("Paciente não encontrado.")

# Funcionalidade para calcular o total de um medicamento no estoque de um paciente
def calcular_total_estoque(nome, medicamento):
    if nome in pacientes and medicamento in pacientes[nome]['estoque']:
        return pacientes[nome]['estoque'][medicamento]
    else:
        # Retorna 0 se o usuário ou medicamento não forem encontrados no estoque
        return 0  


# Funcionalidade para interação com o paciente
def menu():
    while True:
        print("\n=====  Medi+ - Sistema de Estoque de Remédios =====")
        print("1. Cadastrar novo paciente")
        print("2. Adicionar receita médica do paciente")
        print("3. Gerenciar estoque do paciente")
        print("4. Exibir receitas médicas do paciente")
        print("5. Exibir estoque do paciente")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome_usuario = input("Digite o nome do paciente a ser cadastrado: ")
            # .strip() usado para remover espaçamentos 
            cadastrar_usuario(nome_usuario.strip())

        elif opcao == '2':
            nome_usuario = input("Digite o nome do paciente: ")
            receita = input("Digite a receita médica a ser adicionada: ")
            adicionar_receita(nome_usuario, receita)

        elif opcao == '3':
            nome_usuario = input("Digite o nome do paciente: ")
            medicamento = input("Digite o nome do medicamento: ")
            quantidade = int(input("Digite a quantidade de unidades: "))
            operacao = input("Digite '1' para adicionar ao estoque ou '2' para remover: ")
            adicionar = True if operacao == '1' else False
            gerenciar_estoque_usuario(nome_usuario, medicamento, quantidade, adicionar)

        elif opcao == '4':
            nome_usuario = input("Digite o nome do paciente: ")
            exibir_receitas(nome_usuario)

        elif opcao == '5':
            nome_usuario = input("Digite o nome do paciente: ")
            exibir_estoque(nome_usuario)
            medicamento = input("Digite o nome do medicamento para verificar o total no estoque: ")
            total = calcular_total_estoque(nome_usuario, medicamento)
            print(f"Total de {medicamento} no estoque: {total}")

        elif opcao == '6':
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Escolha uma opção válida.")

# Exibir Menu de opções 
if __name__ == "__main__":
    menu()

