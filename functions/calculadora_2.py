def soma(a,b): # Soma
    print("-----------------------------------------")
    print(f"{a} somado por {b} é igual a {a+b}.")
    print("=========================================")
    print("Fim da operação")
    print("=========================================\n")

def subtrai(a,b): # Subtração
    print("-----------------------------------------")
    print(f"{a} subtraido por {b} é igual a {a-b}.")
    print("=========================================")
    print("Fim da operação")
    print("=========================================\n")

def multi(a,b): # Multiplicação
    print("-----------------------------------------")
    print(f"{a} multiplicado por {b} é igual a {a*b}.")
    print("=========================================")
    print("Fim da operação")
    print("=========================================\n")

def dividir(a, b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("-----------------------------------------")
        print("Erro: Tentativa de dividir por zero.")
    except ValueError:
        print("-----------------------------------------")
        print("Erro: Valor inválido informado")
    else:
        print("-----------------------------------------")
        print(f"{a} dividido por {b} é igual a {resultado}.")
    finally:
        print("=========================================")
        print("Fim da operação")
        print("=========================================\n")



operacao = 0
print(f"=========================================\n\
+ = Soma\n\
- = Subtração\n\
X = Multiplicação\n\
/ = Divisão\n\
=========================================")
operacao = input("Digite qual operação deseja realizar: ")
match operacao:
    case '+':
        print("\n=========================================")
        print("Somar dois Números")
        print("=========================================")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        soma(n1,n2)
    case '-':
        print("\n=========================================")
        print("Subtrair dois Números")
        print("=========================================")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        subtrai(n1,n2)
    case 'X' | 'x':
        print("\n=========================================")
        print("Multiplicar dois Números")
        print("=========================================")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        multi(n1,n2)
    case '/':
        print("\n=========================================")
        print("Dividir dois Números")
        print("=========================================")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        dividir(n1,n2)
    case _:
        print("=========================================")
        print("Erro: Valor inválido informado")
        print("=========================================\n")