nome = input("Estimo que esteja bem, favor, digite seu nome:")

resposta = input (f"Olá {nome}, você está entrando em um projeto de teste para Commit Você deseja continuar?")

if resposta.lower() == "sim":
    print ("Quem bom que deseja continuar, é um prazer tê-lo nesse projeto")

elif resposta.lower() == "não":
    print ("ótimo, agradecemos a sua curiosidade, obrigado!")

else: ("Resposta invalida, favor responder 'sim' ou 'não', obrigado")