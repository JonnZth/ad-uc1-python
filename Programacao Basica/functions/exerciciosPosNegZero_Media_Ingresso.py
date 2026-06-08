def PosNegZero(num):
    print("----------------------------")
    if num < 0:
        print(f"O número {num} é negativo.")
    elif num > 0:
        print(f"O número {num} é positivo.")
    else:
        print(f"O número é zero.")

def Media(num1, num2):
    print("----------------------------")
    # qtd = float(input("Digite a quantidade de notas: "))
    media = (num1+num2)/2
    if media >= 7:
        print(f"O aluno está aprovado, com nota {media}.")
    elif media >= 5:
        print(f"O aluno está de recuperação, com nota {media}.")
    else:
        print(f"O aluno está reprovado, com nota {media}.")

def Ingresso(idade):
    print("----------------------------")
    if idade < 12:
        print("O preço do ingresso é R$ 10,00")
    elif idade <= 12:
        print("O preço do ingresso é R$ 15,00")
    elif idade < 0:
        print("Erro: Valor negativo")
    else:
        print("O preço do ingresso é R$ 20,00")

operacao = -1
num1 = 0
num2 = 0
while operacao not in range(0,3):

    print(f"==============================================\n\
0 = Numero positivo, negativo ou zero;\n\
1 = Media de um aluno;\n\
2 = Valor do Ingresso.\n\
==============================================")
    operacao = int(input("Digite qual operação deseja realizar: "))
    print("==============================================")

    if operacao == 0:
        num1 = float(input("Digite um Número: "))
        PosNegZero(num1)
    elif operacao == 1:
        num1 = float(input("Digite a primeira nota: "))
        num2 = float(input("Digite a segunda nota: "))
        Media(num1, num2)
    elif operacao == 2:
        num1 = float(input("Digite um a idade do comprador: "))
        Ingresso(num1)
    else:
        print("Erro: Valor inválido")
        
print("==============================================")