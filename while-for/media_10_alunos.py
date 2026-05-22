NUMEROALUNOS = 10
nota1 = 0
nota2 = 0
media = 0
media_total = 0

print(f"\n=======================================\nInicio da turma com {NUMEROALUNOS} alunos\n=======================================")

for i in range(0,NUMEROALUNOS,1):
    print(f"---- Calculo de média do {i+1}º aluno ----")
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno:  "))
    media = (nota1+nota2)/2
    print(f"A média do aluno é igual a:      {media}.")
    media_total += media

media_total = media_total/NUMEROALUNOS
print(f"=======================================\nFim da turma\n=======================================\nMédia da turma: {media_total}.\n")