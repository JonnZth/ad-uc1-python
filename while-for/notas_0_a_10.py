nota = float(input("Digite uma nota: "))

while nota < 0 or nota > 10:
    print("Errado, nota fora do padrão (0 a 10).")
    nota = float(input("Digite uma nota: "))

print("Nota aceita.")