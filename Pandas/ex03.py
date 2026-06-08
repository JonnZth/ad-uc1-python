# Crie um dataframe com nomes de alunos com as chaves 'nome', 'prova1', 'prova2' e 'prova3'
# dar oportunidade pro usuario escolher o numero de alunos e fazer o input dos alunos
# mostre em forma de dataframe
import pandas as pd

nomes = []
prova1 = []
prova2 = []
prova3 = []
medias = []

print("\n=========================================")
qtd_alunos = int(input("Digite quantos alunos deseja cadastrar: "))

for i in range(qtd_alunos):
    print(f"========= Cadastro do {i+1}º aluno =========")
    nome = input("Digite o nome do aluno: ")
    # Poderia botar mais um for aqui com até 3 valores e só reutilizar 1 variavel pras tres provas, mas eh.
    p1 = float(input("Digite a nota da primeira prova: "))
    p2 = float(input("Digite a nota da segunda prova:  "))
    p3 = float(input("Digite a nota da terceira prova: "))
    media = (p1+p2+p3)/3
    nomes.append(nome)
    prova1.append(p1)
    prova2.append(p2)
    prova3.append(p3)
    medias.append(media)

alunos = {
    'nome': nomes,
    'prova1': prova1,
    'prova2': prova2,
    'prova3': prova3,
    'media': medias
}

alunos_dt = pd.DataFrame(alunos)
alunos_dt.index = alunos_dt.index + 1 # Faz com que o identificador da tabela comece de 1 ao invés de 0

print(f"\
=========================================\n\n\
=========================================\n\
{alunos_dt}\n\
=========================================\n")


