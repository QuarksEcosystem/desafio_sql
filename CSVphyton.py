import pandas as pd

# Seu conjunto de dados (substitua este bloco de código com seus dados reais)
data = """Cliente;ID;Tipo;Data da Venda;Categoria;Vendedor;Regional;Duração do Contrato (Meses);Equipe;Valor;
# ... (seu conjunto de dados continua aqui)
"""

# Lendo os dados e removendo espaços extras nos nomes das colunas
df = pd.read_csv(pd.compat.StringIO(data), sep=';', thousands='.', decimal=',').rename(columns=lambda x: x.strip())

# Convertendo a coluna 'Valor' para numérica
df['Valor'] = df['Valor'].replace('[\$,]', '', regex=True).astype(float)

# Agrupando por vendedor e calculando o valor total vendido por cada um
total_vendas_por_vendedor = df.groupby('Vendedor')['Valor'].sum()

# Criando uma tabela ordenada pelo valor total vendido em ordem decrescente
tabela_resumo = pd.DataFrame(total_vendas_por_vendedor.sort_values(ascending=False))

# Renomeando as colunas
tabela_resumo.columns = ['Valor Total Vendido']

# Exibindo a tabela
print(tabela_resumo)


# Identificando o cliente responsável pela venda com maior valor e menor valor
cliente_maior_valor = df.loc[df['Valor'].idxmax()]['Cliente']
cliente_menor_valor = df.loc[df['Valor'].idxmin()]['Cliente']

print(f"Cliente responsável pela venda com maior valor: {cliente_maior_valor}")
print(f"Cliente responsável pela venda com menor valor: {cliente_menor_valor}\n")

# Calculando e imprimindo o valor médio por Tipo de venda
valor_medio_por_tipo = df.groupby('Tipo')['Valor'].mean()
print("Valor médio por Tipo de venda:")
print(valor_medio_por_tipo, '\n')

# Imprimindo o número de vendas realizada por cliente
num_vendas_por_cliente = df['Cliente'].value_counts()
print("Número de vendas realizada por cliente:")
print(num_vendas_por_cliente)
