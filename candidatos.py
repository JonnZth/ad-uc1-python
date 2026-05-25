
candidados = []
for _ in range(0,1): # _ é usado quando o valor da variavel n será usada em nada, é só pra definir a quantidade de repetições. N é necessario, só uma opção
    nome = input("Digite o nome:" )
    nascimento = input("Digite a data de nascimento:" )
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    formacao = input("Digite a formação: ")


    candidato = { 'nome': nome,
                'nascimento': nascimento,
                'telefone': telefone,
                'email': email,
                'formacao': formacao }

    # verificar candidato
    # salvar, ou não, o candidato    

    print(candidato)