def validar_idade(idade):
    """Valida se a idade é um número inteiro positivo."""
    return idade.isdigit()

def validar_sexo(sexo):
    """Valida se o sexo é M ou F."""
    return sexo.strip().upper() in ['M', 'F']

def validar_decisao(decisao):
    """Valida se a decisão é S ou N."""
    return decisao.strip().upper() in ['S', 'N']

def contar_pessoas(idade, sexo, count, countM, countF):
    """Atualiza as contagens de acordo com idade e sexo."""
    if idade >= 18:
        count += 1
    if sexo == 'M':
        countM += 1
    if sexo == 'F' and idade < 20:
        countF += 1
    return count, countM, countF
