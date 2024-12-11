def processa_idade(idade, sexo):
    resultado = {
        "maior_idade": idade >= 18,
        "sexo": sexo,
        "idade": idade
    }
    return resultado

count = countM = countF = 0

while True:
    # Verificação para garantir que a idade seja um número inteiro positivo
    i = input('Digite sua idade: ')
    while not i.isdigit():
        print("Erro: Tente novamente utilizando apenas números para a idade.")
        i = input('Digite sua idade: ')
    i = int(i)  # Convertendo para número inteiro após a verificação

    # Verificação para garantir que o sexo seja M ou F
    s = input('Digite seu sexo [M/F]: ').strip().upper()
    while s not in ['M', 'F']:
        print("Erro: Tente novamente utilizando apenas 'M' ou 'F' para o sexo.")
        s = input('Digite seu sexo [M/F]: ').strip().upper()

    # Lógica de contagem
    if i >= 18:
        count += 1
    if s == 'M':
        countM += 1
    if s == 'F' and i < 20:
        countF += 1

    # Verificação para garantir que o usuário deseja continuar ou não
    d = input('Deseja continuar? [S/N]: ').strip().upper()
    while d not in ['S', 'N']:
        print("Erro: Tente novamente utilizando apenas 'S' ou 'N' para continuar.")
        d = input('Deseja continuar? [S/N]: ').strip().upper()

    # Finalização com condição de saída
    if d == 'N':
        print(f'\nTemos {count} pessoas de maiores cadastradas')
        print(f'Temos {countM} homens cadastrados')
        print(f'Temos {countF} mulheres menores de 20 anos cadastradas')
        print('Finalizando...')
        break


def processamento_idades():
    return None
