import json

def cadastrar_login():
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Carregar dados existentes do arquivo
    try:
        with open('logins.json', 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = {}

    # Adicionar novo login
    dados[nome_usuario] = senha

    # Salvar os dados atualizados no arquivo
    with open('logins.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)

    print("Login cadastrado com sucesso!")

def main():
    while True:
        print("\n1. Cadastrar novo login")
        print("2. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_login()
        elif opcao == '2':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
