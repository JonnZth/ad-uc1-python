def ParImpar(num):
    if (num % 2) == 0:
        print("O número é Par.")
    else:
        print("O número é Impar.")

def FaixaEtaria(num):
    if num < 13:
        print("Criança")
    elif num < 18:
        print("Adolescente")
    elif num < 60:
        print("Adulto")
    else:
        print("Melhor Idade")

def Desconto(num):
    if num >= 500:
        print(f"Desconto de R$ {(num*0.09):.2f} (9%)")
    elif num >= 200:
        print(f"Desconto de R$ {(num*0.08):.2f} (8%)")
    else:
        print(f"Desconto de R$ {(num*0.07):.2f} (7%)")

operacao = -1
num = 0

while operacao not in range(0,3):

    print(f"==============================================\n\
0 = Se um número é Par ou Impar;\n\
1 = Faixa Etaria de um individuo;\n\
2 = Desconto de um Produto.\n\
==============================================")
    operacao = int(input("Digite qual operação deseja realizar: "))
    print("==============================================")

    if operacao == 0:
        num = float(input("Digite um número: "))
        ParImpar(num)
    elif operacao == 1:
        num = float(input("Digite a idade: "))
        FaixaEtaria(num)
    elif operacao == 2:
        num = float(input("Digite o valor do produto: "))
        Desconto(num)
    else:
        print("Erro: Valor inválido")
        
print("==============================================")