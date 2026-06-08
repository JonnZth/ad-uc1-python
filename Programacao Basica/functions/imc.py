def imc(peso, altura):
    return peso / (altura*altura)

def classificar(imc):
    print(f"IMC: {imc:.2f}") # Limita o numero de casas decimais em 2

    if imc > 40:
        print("Obesidade grau III")
    elif imc >= 35:
        print("Obesidade grau II")
    elif imc >= 30:
        print("Obesidade grau I")
    elif imc >= 25:
        print("Acima do peso")
    elif imc >= 18.5:
        print("Peso normal")
    elif imc >= 17:
        print("Abaixo do  peso")
    else:
        print("Muito abaixo do peso")

n = int(input("\nDigite o número de testes: "))
print("==============================")

for i in range(1, n+1):
    peso = float(input("Digite seu peso: ").replace(",",".")) # Seleciona todas as instancias de ',' no input, e troca por '.'
    altura = float(input("Digite sua altura: ").replace(",","."))

    valor_im = imc(peso, altura)
    classificar(valor_im)
    print("==============================")

print("Fim.")
