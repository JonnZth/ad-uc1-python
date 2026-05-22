num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
maior = num1

if maior <= num2:
    maior = num2
if maior <= num3:
    maior = num3

print(f"O maior número é {maior}")

# ------------------ Como a turma fez --------------------
maior = num3

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num3:
    maior = num2

print(f"O maior número é {maior}")