

def cadastrar_usuário():
    usuario = input("Crie um usuário para ter acesso ao projeto: ")
    senha = input("Crie uma senha: ")
    return usuario, senha

def fazer_login(usuario_cadastro, senha_cadastrada):
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite a sua senha: ")

    if usuario == usuario_cadastro and senha == senha_cadastrada:
        print("Acesso Concedido!")
    else:
        print("Usuário ou senha incorretos. Tente novamente.")

def main():
    while True:
        nome = input("Estimo que esteja bem, favor, digite seu nome: ")

        resposta = input(f"Olá {nome}, você está entrando em um projeto de teste para Commit. Você deseja continuar? ")

        if resposta.lower() == "sim":
            idade = input("Que bom que deseja continuar, é um prazer tê-lo nesse projeto. Quantos anos você tem? ")
            idade = int(idade)

            if idade >= 18:
                print("Você é maior de idade, pode prosseguir com o projeto!")
                usuario_cadastro, senha_cadastrada = cadastrar_usuário()

                print("\nUsuário cadastrado com sucesso!")
                print("Agora tente acessar o projeto com seu login.\n")
                fazer_login(usuario_cadastro, senha_cadastrada)
            else:
                print("Você é menor de idade, infelizmente não pode prosseguir.")

        elif resposta.lower() == "não":
            print("Ótimo, agradecemos a sua curiosidade. Obrigado!")

        else:
            print("Resposta inválida, favor responder 'sim' ou 'não', obrigado.")
            break
main()