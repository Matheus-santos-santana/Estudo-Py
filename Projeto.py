import datetime
import pandas as pd

def cadastrar_usuário():
    usuario = input("Crie um usuário para ter acesso ao Sistema: ")
    senha = input("Crie uma senha: ")
    return usuario, senha

def fazer_login(usuario_cadastro, senha_cadastrada):
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite a sua senha: ")

    if usuario == usuario_cadastro and senha == senha_cadastrada:
        print("Acesso Concedido!")
        return True
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
        return False

hora_atual = datetime.datetime.now().hour

if 5 <= hora_atual < 12:
    parte_do_dia = "Bom dia"
elif 12 <= hora_atual < 18:
    parte_do_dia = "Boa Tarde"
else:
    parte_do_dia = "Boa Noite"

def main():
    dados_usuarios = []

    while True:
        nome = input(f"{parte_do_dia} Estimo que esteja bem, favor, digite seu nome completo: ")

        resposta = input(f"Olá {nome}, você está entrando em nosso Sistema InterLink, um sistema de interação entre nossa plataforma e o usuário. Você deseja continuar? ")

        if resposta.lower() == "sim":
            idade = input("É um prazer tê-lo em nosso sistema. Quantos anos você tem? ")
            idade = int(idade)
            
            if idade >= 18:
                print("Você é maior de idade, pode prosseguir com o projeto!")
                usuario_cadastro, senha_cadastrada = cadastrar_usuário()

                cidade = input("De qual cidade você fala? ")
                data_nasc = input("Qual a sua data de Nascimento? (dd/mm/aaaa) ")
                
                print("\nUsuário cadastrado com sucesso!")
                if fazer_login(usuario_cadastro, senha_cadastrada):
                    dados_usuarios.append({
                        "Nome": nome,
                        "Idade": idade,
                        "usuário": usuario_cadastro,
                        "Senha": senha_cadastrada,
                        "Cidade": cidade,
                        "Data de Nascimento": data_nasc})

                    print("\nDados registrados com sucesso!\n")

                print("Agora tente acessar o projeto com seu login.\n")
            
            else:
                print("Acesso negado, esse projeto é somente para maiores de 18 anos. Obrigado!")

        elif resposta.lower() == "não":
            print("Ótimo, agradecemos a sua curiosidade. Obrigado!")

        else:
            print("Resposta inválida, favor responder 'sim' ou 'não', obrigado.")
            continue

        continuar = input("Deseja cadastrar outro usuário? (Sim/Não): ")
        if continuar.lower() != "sim":
            break

    if dados_usuarios:
        df = pd.DataFrame(dados_usuarios)
        print("\nDados dos Usuários Registrados: ")
        print(df)
        
        df.to_csv('usuarios_registrados.csv', index=False)
        print("\nOs dados dos usuários foram salvos no arquivo 'usuarios_registrados.csv'.")

main()
