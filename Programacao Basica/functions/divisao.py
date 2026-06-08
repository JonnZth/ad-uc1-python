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

print("\n=========================================")
print("Dividir dois Números")
print("=========================================")

try:
    n1 = float(input("Digite o Numerador: "))
    n2 = float(input("Digite o Denominador: "))
except ValueError:
        print("=========================================")
        print("Erro: Valor inválido informado")
        print("=========================================\n")
else:
    dividir(n1,n2)