import datetime
import pandas as pd
import os

def carregar_usuarios():
    """Carregar usuários de um arquivo CSV ou criar um novo DataFrame se o arquivo não existir"""
    if os.path.exists('usuarios_registrados.csv'):
        try:
            return pd.read_csv('usuarios_registrados.csv')
        except Exception as e:
            print(f"Erro ao carregar usuários: {e}")
            return pd.DataFrame(columns=["Nome", "Idade", "usuário", "Senha", "Cidade", "Data de Nascimento"])
    return pd.DataFrame(columns=["Nome", "Idade", "usuário", "Senha", "Cidade", "Data de Nascimento"])

def salvar_usuarios(df):
    """Salvar DataFrame de usuários em um arquivo CSV"""
    try:
        df.to_csv('usuarios_registrados.csv', index=False)
        print("\nOs dados dos usuários foram salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar usuários: {e}")

def validar_usuario(usuario_login, senha_login, usuarios_registrados):
    """Validar credenciais do usuário"""
    if usuarios_registrados.empty:
        return False
        
    usuario_login = usuario_login.strip().lower()
    usuarios_registrados['usuário'] = usuarios_registrados['usuário'].str.strip().str.lower()
    
    usuarios_correspondentes = usuarios_registrados[usuarios_registrados['usuário'] == usuario_login]
    if not usuarios_correspondentes.empty:
        return usuarios_correspondentes.iloc[0]['Senha'] == senha_login
    return False

def saudacao_por_horario():
    """Obter saudação apropriada com base no horário do dia"""
    hora_atual = datetime.datetime.now().hour
    if 5 <= hora_atual < 12:
        return "Bom dia"
    elif 12 <= hora_atual < 18:
        return "Boa Tarde"
    else:
        return "Boa Noite"

def cadastrar_novo_usuario(usuarios_registrados):
    """Cadastrar um novo usuário"""
    nome = input(f"{saudacao_por_horario()}! Estimo que esteja bem, favor, digite seu nome completo: ")
    
    try:
        idade = int(input("Quantos anos você tem? "))
        if idade < 18:
            print("Acesso negado. Este projeto é somente para maiores de 18 anos. Obrigado!")
            return None
    except ValueError:
        print("Por favor, digite uma idade válida.")
        return None

    usuario = input("Crie um usuário para ter acesso ao sistema: ").strip()
    if usuario.lower() in usuarios_registrados['usuário'].str.lower().values:
        print("Este usuário já existe. Por favor, escolha outro.")
        return None

    senha = input("Crie uma senha: ")
    cidade = input("De qual cidade você fala? ")
    data_nasc = input("Qual a sua data de nascimento? (dd/mm/aaaa) ")

    return {
        "Nome": nome,
        "Idade": idade,
        "usuário": usuario,
        "Senha": senha,
        "Cidade": cidade,
        "Data de Nascimento": data_nasc
    }

def main():
    usuarios_registrados = carregar_usuarios()
    
    while True:
        validar_cadastro = input("\nVocê já possui cadastro? (Sim/Não): ").strip().lower()

        if validar_cadastro == "sim":
            usuario_login = input("Digite seu nome de usuário: ")
            senha_login = input("Digite sua senha: ")

            if validar_usuario(usuario_login, senha_login, usuarios_registrados):
                dados_usuario = usuarios_registrados[usuarios_registrados['usuário'].str.lower() == usuario_login.lower()].iloc[0]
                print(f"\nBem-vindo(a), {dados_usuario['Nome']}!")
                print(f"Suas informações são:")
                print(f"Idade: {dados_usuario['Idade']}")
                print(f"Cidade: {dados_usuario['Cidade']}")
                print(f"Data de Nascimento: {dados_usuario['Data de Nascimento']}")
            else:
                print("Login falhou. Usuário ou senha incorretos.")

        elif validar_cadastro == "não":
            novo_usuario = cadastrar_novo_usuario(usuarios_registrados)
            if novo_usuario:
                usuarios_registrados = pd.concat([usuarios_registrados, 
                                               pd.DataFrame([novo_usuario])], 
                                               ignore_index=True)
                salvar_usuarios(usuarios_registrados)
                print("\nUsuário cadastrado com sucesso!")
        else:
            print("Opção inválida. Por favor, responda 'sim' ou 'não'.")

        continuar = input("\nDeseja continuar? (Sim/Não): ")
        if continuar.lower() != "sim":
            break

    print("\nObrigado por usar nosso sistema!")

if __name__ == "__main__":
    main()