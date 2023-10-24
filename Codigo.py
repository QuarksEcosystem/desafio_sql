#Bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Leitura do arquivo
arquivo = "/home/juliana/Documents/CVsProcessosSeletivos/SysmapTriggoAI/Desafio/DB_Teste.csv"
vendas = pd.read_csv(arquivo, delimiter=";")

#Criação da tabela auxiliar
df = vendas.copy()
df[['Moeda', 'Valor']] = df['Valor'].str.split('$', expand=True)
df['Ano'] = df['Data da Venda']
df['Mes'] = df['Data da Venda']

#Exclusão dos pontos no campo Valor
shape = df.shape
linhas = shape[0]
i = 0
for i in range(linhas): 
    linha = df['Valor'][i]
    linha = linha.replace('.', '')
    linha = linha.replace(',', '.')
    df['Valor'][i] = linha
    df['Ano'][i] = df['Ano'][i][6:10]
    df['Mes'][i] = df['Mes'][i][3:5]

#Conversão do campo Valor de object para float
df["Valor"] = df["Valor"].astype('float64')

#Criação da tabela auxiliar
auxiliar = df.pivot_table(values="Valor", index="Vendedor", aggfunc=np.sum)
auxiliar = auxiliar.sort_values('Valor', ascending=False)

#Maior e menor venda
maior_venda = df.max()
vendedor = maior_venda['Vendedor']
print("Vendedor responsável pela venda de maior valor: ", vendedor)
menor_venda = df.min()
vendedor = menor_venda['Vendedor']
print("Vendedor responsável pela venda de menor valor: ", vendedor)

#Média por tipo de serviço
df.pivot_table(values="Valor", index="Tipo", aggfunc=np.mean)

#Número de vendas por cliente
df["Cliente"].value_counts()

df.pivot_table(values="Valor", index=["Ano", "Mes"], aggfunc=np.mean)



