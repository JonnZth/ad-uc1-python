# Ler entrada de usuário

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1+nota2+nota3+nota4)/4

print(f"\nA média é {media}")

if (media < 5):
    print("Voce foi reprovado\n")
elif (media < 7):
    print("Você está de recuperação\n")
else:
    print("Você foi aprovado\n")