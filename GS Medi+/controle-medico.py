
# Lista para armazenar informações dos usuários, suas receitas e estoque
usuarios = {}

# Cadastro de um novo usuário
def cadastrar_usuario(nome):
    if nome not in usuarios:
        usuarios[nome] = {'receitas': [], 'estoque': {}}
        print(f"Usuário '{nome}' cadastrado com sucesso.")
    else:
        print("Usuário já existe.")

# Funcionalidade para adicionar uma receita médica a um usuário
def adicionar_receita(nome, receita):
    if nome in usuarios:
        usuarios[nome]['receitas'].append(receita)
        print(f"Receita médica adicionada para o usuário '{nome}'.")
    else:
        print("Usuário não encontrado.")

# Funcionalidade para adicionar/remover medicamentos ao estoque de um usuário
def gerenciar_estoque_usuario(nome, medicamento, quantidade, adicionar=True):
    if nome in usuarios:
        if adicionar:
            if medicamento in usuarios[nome]['estoque']:
                usuarios[nome]['estoque'][medicamento] += quantidade
            else:
                usuarios[nome]['estoque'][medicamento] = quantidade
            print(f"{quantidade} unidades de {medicamento} adicionadas ao estoque de '{nome}'.")
        else:
            if medicamento in usuarios[nome]['estoque'] and usuarios[nome]['estoque'][medicamento] >= quantidade:
                usuarios[nome]['estoque'][medicamento] -= quantidade
                print(f"{quantidade} unidades de {medicamento} removidas do estoque de '{nome}'.")
            else:
                print("Quantidade insuficiente no estoque.")
    else:
        print("Usuário não encontrado.")

# Funcionalidade para exibir as receitas médicas de um usuário
def exibir_receitas(nome):
    if nome in usuarios:
        print(f"\nReceitas médicas do usuário '{nome}':")
        for receita in usuarios[nome]['receitas']:
            print(receita)
    else:
        print("Usuário não encontrado.")

# Funcionalidade para exibir o estoque de um usuário
def exibir_estoque(nome):
    if nome in usuarios:
        print(f"\nEstoque atual do usuário '{nome}':")
        if usuarios[nome]['estoque']:
            for medicamento, quantidade in usuarios[nome]['estoque'].items():
                print(f"{medicamento}: {quantidade} unidades")
        else:
            print("O estoque está vazio para este usuário.")
    else:
        print("Usuário não encontrado.")

# Funcionalidade para interação com o usuário
def menu():
    while True:
        print("\n===== Sistema de Controle de Usuários e Estoque de Remédios =====")
        print("1. Cadastrar novo usuário")
        print("2. Adicionar receita médica a um usuário")
        print("3. Gerenciar estoque de um usuário")
        print("4. Exibir receitas médicas de um usuário")
        print("5. Exibir estoque de um usuário")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome_usuario = input("Digite o nome do usuário a ser cadastrado: ")
            # .strip() usado para remover espaçamentos 
            cadastrar_usuario(nome_usuario.strip())
        elif opcao == '2':
            nome_usuario = input("Digite o nome do usuário: ")
            receita = input("Digite a receita médica a ser adicionada: ")
            adicionar_receita(nome_usuario, receita)
        elif opcao == '3':
            nome_usuario = input("Digite o nome do usuário: ")
            medicamento = input("Digite o nome do medicamento: ")
            quantidade = int(input("Digite a quantidade a ser gerenciada: "))
            operacao = input("Digite 'adicionar' para adicionar ao estoque ou 'remover' para remover: ")
            adicionar = True if operacao.lower() == 'adicionar' else False
            gerenciar_estoque_usuario(nome_usuario, medicamento, quantidade, adicionar)
        elif opcao == '4':
            nome_usuario = input("Digite o nome do usuário: ")
            exibir_receitas(nome_usuario)
        elif opcao == '5':
            nome_usuario = input("Digite o nome do usuário: ")
            exibir_estoque(nome_usuario)
        elif opcao == '6':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Escolha uma opção válida.")

# Exibir Menu de opções 
if __name__ == "__main__":
    menu()

