import pandas as pd

cargos = []
salarios = []

qtd_dados = int(input("Digite quantos dados deseja cadastrar: "))

for i in range(qtd_dados):
    print(f"Cadastro {i+1}: ")
    cargo = input("Digite o nome do cargo: ")
    salario = float(input("Digite o salário do cargo: "))
    cargos.append(cargo)
    salarios.append(salario)

dados = {
    'cargos': cargos,
    'salarios': salarios
}

dados_emp = pd.DataFrame(dados)
dados_emp.index = dados_emp.index + 1 # Faz com que o identificador da tabela comece de 1 ao invés de 0
print(dados_emp)