from sqlalchemy import create_engine
import pandas as pd

host = 'localhost'
user = 'root'
password = ''
database = 'aulaPandas'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

df = pd.read_sql("Select * from odontologia", con=engine)

filtro=df[
    (df['uf'] == 'DF') & (df['titulacao'] == 'TÍTULO DE ESPECIALISTA') # Filtros de informação
    ][
        ['nome','titulacao','municipio'] # Quais colunas mostrar
        ]

print(filtro)