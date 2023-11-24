
import pandas as pd


data = pd.read_csv("DB_Teste.csv", sep=";", decimal=",")
data = data.dropna(axis=1, how='all')
data['Duração do Contrato (Meses)'] = data['Duração do Contrato (Meses)'].astype(int)
#data['Valor'] = data['Valor'].replace('[\$,]', '', regex=True).astype(float)
data['Valor'] = data['Valor'].str.replace(' ', '').str.replace('R\$', '', regex=True).str.replace('.', '').str.replace(',', '.').astype(float)
data['Data da Venda'] = pd.to_datetime(data['Data da Venda'], format='%d/%m/%Y')

print(data.dtypes)
