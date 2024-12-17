import datetime
import pandas as pd
import os

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

def validar_usuario(usuario_login, senha_login, usuarios_registrados):    
    usuario_login = usuario_login.strip().lower()
    senha_login = senha_login.strip()
    
    usuarios_registrados['usuário'] = usuarios_registrados['usuário'].str.strip().str.lower()
    
    if usuario_login in usuarios_registrados['usuário'].values:        
        senha_registrada = usuarios_registrados[usuarios_registrados['usuário'] == usuario_login]['Senha'].values[0]

        if senha_login == senha_registrada:
            return True
    return False

def main():
    hora_atual = datetime.datetime.now().hour

    if 5 <= hora_atual < 12:
        parte_do_dia = "Bom dia"
    elif 12 <= hora_atual < 18:
        parte_do_dia = "Boa Tarde"
    else:
        parte_do_dia = "Boa Noite"

    dados_usuarios = []
    
    if os.path.exists('usuarios_registrados.csv'):
        usuarios_registrados = pd.read_csv('usuarios_registrados.csv')
    else:
        usuarios_registrados = pd.DataFrame(columns=["Nome", "Idade", "usuário", "Senha", "Cidade", "Data de Nascimento"])

    while True:
        validar_cadastro = input("Você já possui cadastro? (Sim/Não): ").strip().lower()

        if validar_cadastro == "sim":
            usuario_login = input("Digite seu nome de usuário: ")
            senha_login = input("Digite sua senha: ")

            if validar_usuario(usuario_login, senha_login, usuarios_registrados):
                print(f"Acesso concedido, {usuario_login}!")

                nome = usuario_login
                idade = usuarios_registrados[usuarios_registrados['usuário'] == usuario_login]['Idade'].values[0]
                cidade = usuarios_registrados[usuarios_registrados['usuário'] == usuario_login]['Cidade'].values[0]
                data_nasc = usuarios_registrados[usuarios_registrados['usuário'] == usuario_login]['Data de Nascimento'].values[0]
                print(f"Bem-vindo {nome}, suas informações são:")
                print(f"Idade: {idade}")
                print(f"Cidade: {cidade}")
                print(f"Data de Nascimento: {data_nasc}")

            else:
                print("Login falhou. Usuário ou senha incorretos.")
                continue
                

        else:
            print("Por favor, realize seu cadastro primeiro.")
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