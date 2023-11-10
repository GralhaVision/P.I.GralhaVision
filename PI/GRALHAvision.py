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
