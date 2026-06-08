
def soma(a,b): # Soma
    return a + b

def subtrai(a,b): # Subtração
    return a - b

def multi(a,b): # Multiplicação
    return a * b

def divi(a,b): # Divisão
    if b == 0:
        return "Erro. Tentativa de dividir por zero."
    return a / b

def media(a,b): # Média de dois números
    return (a + b)/2
# -------------------------------------------------------------------------- #
print("=======================\n0 = Soma\n1 = Subtração\n2 = Multiplicação\n3 = Divisão\n4 = Média de dois números\n=======================")
operacao = int(input("Digite qual operação deseja realizar: "))

if operacao == 0 or operacao == 1 or operacao == 2 or operacao == 3 or operacao == 4:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if operacao == 0:
        print(f"Os números {num1} e {num2} somados resultam em: {soma(num1,num2)}")
    elif operacao == 1:
        print(f"Os números {num1} e {num2} subtraidos resultam em: {subtrai(num1,num2)}")
    elif operacao == 2:
        print(f"Os números {num1} e {num2} multiplicados resultam em: {multi(num1,num2)}")
    elif operacao == 3:
        print(f"Os números {num1} e {num2} divididos resultam em: {divi(num1,num2)}")
    elif operacao == 4:
        print(f"A média dos números {num1} e {num2} resulta em: {media(num1,num2)}")
else:
    print("Operação Invalida.")