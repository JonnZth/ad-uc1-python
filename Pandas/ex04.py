import pandas as pd

df = pd.read_csv('ClassicDisco.csv') # define o dataframe para ler os valores dentro do csv especificado

# print(df.to_string()) # O to_string faz com que apareça tudo no csv ao inves de só a versão simplificada
# filtro = df['Artist']

# print(filtro.to_string(index=False)) # remove o index do dataframe

# filtro = df[df['Year'] >1980]

# filtro = df[
#     df['Year'] >1980
#     ][
#         ['Year','Track']]

# filtro = df[
#     df['Artist'] == 'Aretha Franklin'
#     ]\
#         [
#             ['Track','Artist','Year']] # Multiplas Colunas

filtro = df[
    (df['Artist'] == 'Aretha Franklin') & (df['Year'] >1973) # Multiplos Filtros
    ]\
        [
            ['Track','Artist','Year']]


print(filtro.to_string())
