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


def main():
    while True:
        print("-"*15+"BEM VINDOS A GRALHAVISION"+15*"-")
        print("1. Criar cadastro")
        print("2. Editar cadastro")
        print("3. Excluir cadastro")
        print("4. Sair")
        print("-"*56)
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_cadastro()
        elif opcao == '2':
            email = input("Informe o email: ")
            senha = input("Informe a senha: ")
            editar_cadastro(email, senha)
        elif opcao == '3':
            email = input("Informe o email: ")
            senha = input("Informe a senha: ")
            excluir_cadastro(email, senha)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")
        print("-"*56)
        limpar_tela()


main()