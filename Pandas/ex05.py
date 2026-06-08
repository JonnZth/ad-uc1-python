import pandas as pd

df = pd.read_excel('bancos.xlsx') # define o dataframe para ler os valores dentro do arquivo excel especificado

# print(df.to_string())

# Descreva somente o nome dos bancos

filtro = df['Banco']

print(filtro)