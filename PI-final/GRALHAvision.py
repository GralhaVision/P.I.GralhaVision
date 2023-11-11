import json
import os
import smtplib
import email.message


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


def adicionar_produto():
    nome_produto = input("Nome do produto: ")
    tipo_produto = input("Tipo do produto (lente, armação, etc.): ")
    fornecedor_produto = input("CNPJ do fornecedor do produto: ")
    tempo_entrega = input("Tempo de entrega estimado (em dias): ")
    novo_produto = {
        'nome': nome_produto,
        'tipo': tipo_produto,
        'fornecedor': fornecedor_produto,
        'tempo_entrega': tempo_entrega
    }
    try:
        with open('produtos.json', 'r') as arquivo:
            produtos = json.load(arquivo)
    except FileNotFoundError:
        produtos = []
    produtos.append(novo_produto)
    with open('produtos.json', 'w') as arquivo:
        json.dump(produtos, arquivo, indent=4)
    print("Produto adicionado com sucesso!")


def listar_produtos():
    try:
        with open('produtos.json', 'r') as arquivo:
            produtos = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum produto encontrado.")
        return
    print("Lista de Produtos:")
    for produto in produtos:
        print(
            f"Nome: {produto['nome']}, Tipo: {produto['tipo']}, Fornecedor: {produto['fornecedor']}, Tempo de Entrega: {produto['tempo_entrega']} dias")


def editar_produto():
    try:
        with open('produtos.json', 'r') as arquivo:
            produtos = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum produto encontrado.")
        return
    nome_alterar = input("Informe o nome do produto a ser editado: ")

    for produto in produtos:
        if produto['nome'] == nome_alterar:
            novo_nome = input("Novo nome do produto: ")
            novo_tipo = input("Novo tipo do produto: ")
            novo_fornecedor = input("Novo CNPJ do fornecedor: ")
            novo_tempo_entrega = input("Novo tempo de entrega estimado (em dias): ")
            produto['nome'] = novo_nome
            produto['tipo'] = novo_tipo
            produto['fornecedor'] = novo_fornecedor
            produto['tempo_entrega'] = novo_tempo_entrega
            with open('produtos.json', 'w') as arquivo:
                json.dump(produtos, arquivo, indent=4)
            print("Produto editado com sucesso!")
            return
    print("Produto não encontrado.")


def excluir_produto():
    try:
        with open('produtos.json', 'r') as arquivo:
            produtos = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum produto encontrado.")
        return
    nome_excluir = input("Informe o nome do produto a ser excluído: ")
    for produto in produtos:
        if produto['nome'] == nome_excluir:
            produtos.remove(produto)
            with open('produtos.json', 'w') as arquivo:
                json.dump(produtos, arquivo, indent=4)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado.")


def mprodutos():
    while True:
        limpar_tela()
        print("-" * 15 + "MENU PRODUTOS" + 15 * "-")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Editar Produto")
        print("4. Excluir Produto")
        print("5. Voltar ao Menu Principal")
        print("-" * 56)
        opcao_produtos = input("Escolha uma opção: ")
        if opcao_produtos == '1':
            adicionar_produto()
        elif opcao_produtos == '2':
            listar_produtos()
        elif opcao_produtos == '3':
            editar_produto()
        elif opcao_produtos == '4':
            excluir_produto()
        elif opcao_produtos == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")


arquivo_json = "ordens_de_servico.json"


def carregar_ordens_de_servico():
    try:
        with open(arquivo_json, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def salvar_ordens_de_servico(ordens_de_servico):
    with open(arquivo_json, 'w') as file:
        json.dump(ordens_de_servico, file, indent=4)


ordens_de_servico = carregar_ordens_de_servico()


def criar_os():
    numero_os = input("Digite o número da OS: ")
    descricao = input("Digite a descrição da OS: ")
    print("Produtos disponíveis:")
    listar_produtos()
    nome_produto_os = input("Digite o nome do produto para a OS: ")
    osvc = {
        'Número': numero_os,
        'Descrição': descricao,
        'Produto': nome_produto_os
    }
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


def criar_cliente():
    nome = input("Nome do cliente: ")
    email = input("Email do cliente: ")
    senha = input("Senha do cliente: ")
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return
    novo_cliente = {
        'nome': nome,
        'email': email,
        'senha': senha
    }
    try:
        with open('cadastros.json', 'r') as arquivo:
            clientes = json.load(arquivo)
    except FileNotFoundError:
        clientes = []
    for cliente in clientes:
        if cliente['email'] == email:
            print("Esse email já está cadastrado.")
            return
    clientes.append(novo_cliente)
    with open('cadastros.json', 'w') as arquivo:
        json.dump(clientes, arquivo, indent=4)
    print("Cliente criado com sucesso!")


def listar_clientes():
    try:
        with open('cadastros.json', 'r') as arquivo:
            clientes = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum cliente encontrado.")
        return
    print("Lista de Clientes:")
    for cliente in clientes:
        print(f"Nome: {cliente['nome']}, Email: {cliente['email']}")


def editar_cliente(email, senha):
    try:
        with open('cadastros.json', 'r') as arquivo:
            clientes = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum cliente encontrado.")
        return
    for cliente in clientes:
        if cliente['email'] == email and cliente['senha'] == senha:
            novo_nome = input("Novo nome do cliente: ")
            cliente['nome'] = novo_nome
            with open('cadastros.json', 'w') as arquivo:
                json.dump(clientes, arquivo, indent=4)
            print("Cliente editado com sucesso!")
            return
    print("Cliente não encontrado.")


def excluir_cliente(email, senha):
    try:
        with open('cadastros.json', 'r') as arquivo:
            clientes = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum cliente encontrado.")
        return
    for cliente in clientes:
        if cliente['email'] == email and cliente['senha'] == senha:
            clientes.remove(cliente)

            with open('cadastros.json', 'w') as arquivo:
                json.dump(clientes, arquivo, indent=4)

            print("Cliente excluído com sucesso!")
            return
    print("Cliente não encontrado.")

def mclientes():
    while True:
        limpar_tela()
        print("-" * 15 + "MENU CLIENTES" + 15 * "-")
        print("1. Criar Cliente")
        print("2. Listar Clientes")
        print("3. Editar Cliente")
        print("4. Excluir Cliente")
        print("5. Voltar ao Menu Principal")
        print("-" * 56)
        opcao_clientes = input("Escolha uma opção: ")
        if opcao_clientes == '1':
            criar_cliente()
        elif opcao_clientes == '2':
            listar_clientes()
        elif opcao_clientes == '3':
            email = input("Informe o email do cliente: ")
            senha = input("Informe a senha do cliente: ")
            editar_cliente(email, senha)
        elif opcao_clientes == '4':
            email = input("Informe o email do cliente: ")
            senha = input("Informe a senha do cliente: ")
            excluir_cliente(email, senha)
        elif opcao_clientes == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")


def enviar_email():

    nome = input("Informe o nome do proprietário: ")
    end = input("Informe o email do proprietário: ")
    cnpj = input("Informe o CNPJ do proprietário: ")
    ass = input("Relate os erros ou dúvidas sobre o software: ")
    corpo_email = """
    <p>Nome: {} </p>
    <p>Email: {} </p>
    <p>CNPJ: {} </p>
    <p>Assunto: {} </p>
    """.format(nome, end, cnpj, ass)
    msg = email.message.Message()
    msg['Subject'] = "SUPORTE: GRALHA VISION"
    msg['From'] = 'suporte.gralha@gmail.com'
    msg['To'] = 'visiongralha@gmail.com', 'suporte.gralha@gmail.com'
    password = 'tsxkpujjzchdnszh'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


def menu_logado():
    while True:
        limpar_tela()
        print("-" * 15 + "MENU PRINCIPAL" + 15 * "-")
        print("1. Fornecedores")
        print("2. Produtos")
        print("3. Ordens de Serviço (OS)")
        print("4. Clientes")
        print("5. Suporte")
        print("6. Sair")
        print("-" * 56)
        opcao_menu = input("Escolha uma opção: ")
        if opcao_menu == '1':
            print("Você selecionou Fornecedores.")
            input("Pressione Enter para continuar...")
            limpar_tela()
            mfornecedores()
        elif opcao_menu == '2':
            print("Você selecionou Produtos.")
            input("Pressione Enter para continuar...")
            limpar_tela()
            mprodutos()
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
            print("Você selecionou Clientes.")
            input("Pressione Enter para continuar...")
            limpar_tela()
            mclientes()
        elif opcao_menu == '5':
            print("Você selecionou Suporte.")
            input("Pressione Enter para continuar...")
            limpar_tela()
            enviar_email()
        elif opcao_menu == '6':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def main():
    while True:
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
