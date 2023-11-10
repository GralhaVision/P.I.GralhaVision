import json
import os


def limpar_tela():
    os.system('cls')


def criar_cadastro():
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return
    novo_cadastro = {
        'nome': nome,
        'email': email,
        'senha': senha
    }
    try:
        with open('cadastros.json', 'r') as arquivo:
            cadastros = json.load(arquivo)
    except FileNotFoundError:
        cadastros = []
    for cadastro in cadastros:
        if cadastro['email'] == email:
            print("Esse email já está cadastrado.")
            return
    cadastros.append(novo_cadastro)
    with open('cadastros.json', 'w') as arquivo:
        json.dump(cadastros, arquivo, indent=4)
    print("Cadastro criado com sucesso!")


def editar_cadastro(email, senha):
    try:
        with open('cadastros.json', 'r') as arquivo:
            cadastros = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum cadastro encontrado.")
        return
    for cadastro in cadastros:
        if cadastro['email'] == email and cadastro['senha'] == senha:
            novo_nome = input("Novo nome: ")
            cadastro['nome'] = novo_nome
            with open('cadastros.json', 'w') as arquivo:
                json.dump(cadastros, arquivo, indent=4)
            print("Cadastro editado com sucesso!")
            return
    print("Cadastro não encontrado.")


def excluir_cadastro(email, senha):
    try:
        with open('cadastros.json', 'r') as arquivo:
            cadastros = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum cadastro encontrado.")
        return
    for cadastro in cadastros:
        if cadastro['email'] == email and cadastro['senha'] == senha:
            cadastros.remove(cadastro)
            with open('cadastros.json', 'w') as arquivo:
                json.dump(cadastros, arquivo, indent=4)
            print("Cadastro excluído com sucesso!")
            return
    print("Cadastro não encontrado.")


def login(email, senha):
    try:
        with open('cadastros.json', 'r') as arquivo:
            cadastros = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum cadastro encontrado.")
        return False
    for cadastro in cadastros:
        if cadastro['email'] == email and cadastro['senha'] == senha:
            print("Login bem-sucedido!")
            return True
    print("Email ou senha inválidos.")
    return False


def adicionar_fornecedor():
    nome_fornecedor = input("Nome do fornecedor: ")
    cnpj_fornecedor = input("CNPJ do fornecedor: ")
    novo_fornecedor = {
        'nome': nome_fornecedor,
        'cnpj': cnpj_fornecedor
    }
    try:
        with open('fornecedores.json', 'r') as arquivo:
            fornecedores = json.load(arquivo)
    except FileNotFoundError:
        fornecedores = []
    fornecedores.append(novo_fornecedor)
    with open('fornecedores.json', 'w') as arquivo:
        json.dump(fornecedores, arquivo, indent=4)
    print("Fornecedor adicionado com sucesso!")


def listar_fornecedores():
    try:
        with open('fornecedores.json', 'r') as arquivo:
            fornecedores = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum fornecedor encontrado.")
        return
    print("Lista de Fornecedores:")
    for fornecedor in fornecedores:
        print(f"Nome: {fornecedor['nome']}, CNPJ: {fornecedor['cnpj']}")


def editar_fornecedor():
    try:
        with open('fornecedores.json', 'r') as arquivo:
            fornecedores = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum fornecedor encontrado.")
        return
    cnpj_alterar = input("Informe o CNPJ do fornecedor a ser editado: ")
    for fornecedor in fornecedores:
        if fornecedor['cnpj'] == cnpj_alterar:
            novo_nome = input("Novo nome do fornecedor: ")
            fornecedor['nome'] = novo_nome
            with open('fornecedores.json', 'w') as arquivo:
                json.dump(fornecedores, arquivo, indent=4)
            print("Fornecedor editado com sucesso!")
            return
    print("Fornecedor não encontrado.")


def excluir_fornecedor():
    try:
        with open('fornecedores.json', 'r') as arquivo:
            fornecedores = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum fornecedor encontrado.")
        return
    cnpj_excluir = input("Informe o CNPJ do fornecedor a ser excluído: ")
    for fornecedor in fornecedores:
        if fornecedor['cnpj'] == cnpj_excluir:
            fornecedores.remove(fornecedor)
            with open('fornecedores.json', 'w') as arquivo:
                json.dump(fornecedores, arquivo, indent=4)
            print("Fornecedor excluído com sucesso!")
            return
    print("Fornecedor não encontrado.")


def mfornecedores():
    while True:
        limpar_tela()
        print("-" * 15 + "MENU FORNECEDORES" + 15 * "-")
        print("1. Adicionar Fornecedor")
        print("2. Listar Fornecedores")
        print("3. Editar Fornecedor")
        print("4. Excluir Fornecedor")
        print("5. Voltar ao Menu Principal")
        print("-" * 56)
        opcao_fornecedores = input("Escolha uma opção: ")
        if opcao_fornecedores == '1':
            adicionar_fornecedor()
        elif opcao_fornecedores == '2':
            listar_fornecedores()
        elif opcao_fornecedores == '3':
            editar_fornecedor()
        elif opcao_fornecedores == '4':
            excluir_fornecedor()
        elif opcao_fornecedores == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")


arquivo_json = "ordens_de_servico.json"


def carregar_ordens_de_servico():
    try:
        with open(ordens_de_servico, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def salvar_ordens_de_servico(ordens_de_servico):
    with open(arquivo_json, 'w') as file:
        json.dump(ordens_de_servico, file)


ordens_de_servico = carregar_ordens_de_servico()


def criar_os():
    numero_os = input("Digite o número da OS: ")
    descricao = input("Digite a descrição da OS: ")
    osvc = {'Número': numero_os, 'Descrição': descricao}
    ordens_de_servico.append(osvc)

    print(f"OS {numero_os} criada com sucesso!")
    salvar_ordens_de_servico(ordens_de_servico)


def visualizar_os():
    if not ordens_de_servico:
        print("Nenhuma OS encontrada.")
    else:
        for osvc in ordens_de_servico:
            print(f"Número: {osvc['Número']}, Descrição: {osvc['Descrição']}")


def atualizar_os():
    numero_os = input("Digite o número da OS que deseja atualizar: ")
    for osvc in ordens_de_servico:
        if osvc['Número'] == numero_os:
            nova_descricao = input("Digite a nova descrição: ")
            osvc['Descrição'] = nova_descricao
            print(f"OS {numero_os} atualizada com sucesso!")
            salvar_ordens_de_servico(ordens_de_servico)
            return
    print(f"OS {numero_os} não encontrada.")


def excluir_os():
    numero_os = input("Digite o número da OS que deseja excluir: ")
    for osvc in ordens_de_servico:
        if osvc['Número'] == numero_os:
            ordens_de_servico.remove(os)
            print(f"OS {numero_os} excluída com sucesso!")
            salvar_ordens_de_servico(ordens_de_servico)
            return
    print(f"OS {numero_os} não encontrada.")


def menu_logado():
    while True:
        limpar_tela()
        print("-" * 15 + "MENU PRINCIPAL" + 15 * "-")
        print("1. Fornecedores")
        print("2. Produtos")
        print("3. Ordens de Serviço (OS)")
        print("4. Usuários")
        print("5. Suporte")
        print("6. Sair")
        print("-" * 56)
        opcao_menu = input("Escolha uma opção: ")
        if opcao_menu == '1':
            print("Você selecionou Fornecedores.")
            input("Pressione Enter para continuar...")
            mfornecedores()
        elif opcao_menu == '2':
            print("Você selecionou Produtos.")
            input("Pressione Enter para continuar...")
        elif opcao_menu == '3':
            print("Você selecionou Ordens de Serviço (OS).")
            input("Pressione Enter para continuar...")
            while True:
                limpar_tela()
                print("-" * 15 + "MENU DE ORDENS DE SERVIÇO (OS)" + 15 * "-")
                print("1. Criar OS")
                print("2. Visualizar OS")
                print("3. Atualizar OS")
                print("4. Excluir OS")
                print("5. Voltar ao Menu Principal")
                print("-" * 56)
                opcao_os = input("Escolha uma opção: ")
                if opcao_os == '1':
                    criar_os()
                elif opcao_os == '2':
                    visualizar_os()
                elif opcao_os == '3':
                    atualizar_os()
                elif opcao_os == '4':
                    excluir_os()
                elif opcao_os == '5':
                    print("Voltando ao Menu Principal.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif opcao_menu == '4':
            print("Você selecionou Usuários.")
            input("Pressione Enter para continuar...")
        elif opcao_menu == '5':
            print("Você selecionou Suporte.")
            input("Pressione Enter para continuar...")
        elif opcao_menu == '6':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def main():
    while True:
        limpar_tela()
        print("-"*15+"BEM VINDOS A GRALHAVISION"+15*"-")
        print("1. Login")
        print("2. Cadastro")
        print("3. Sair")
        print("-"*56)
        opcao_principal = input("Escolha uma opção: ")
        if opcao_principal == '1':
            email = input("Informe o email: ")
            senha = input("Informe a senha: ")
            login(email, senha)
            if login(email, senha):
                print("Login bem-sucedido!")
                input("Pressione Enter para continuar...")
                menu_logado()
            else:
                print("Email ou senha inválidos. Tente novamente.")
                input("Pressione Enter para continuar...")
        elif opcao_principal == '2':
            print("1. Criar cadastro")
            print("2. Editar cadastro")
            print("3. Excluir cadastro")
            print("-"*56)
            opcao_cadastro = input("Escolha uma opção: ")
            if opcao_cadastro == '1':
                criar_cadastro()
            elif opcao_cadastro == '2':
                email = input("Informe o email: ")
                senha = input("Informe a senha: ")
                editar_cadastro(email, senha)
            elif opcao_cadastro == '3':
                email = input("Informe o email: ")
                senha = input("Informe a senha: ")
                excluir_cadastro(email, senha)
            else:
                print("Opção inválida. Tente novamente.")
        elif opcao_principal == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")
        print("-"*56)


main()
