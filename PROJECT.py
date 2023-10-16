import pandas as pd


def main():
    
    # Leitura do arquivo CSV disponibilizado, que deverá estar no mesmo local do arquivo para que possa ser utilizado
    df = pd.read_csv("DB_Teste.csv", sep = ';')
    
    # Retira os pontos e vírgulas do campo valor
    df['Valor'] = df['Valor'].str.replace('R$', '').str.replace('.', '').str.replace(',', '.').astype(float)
    
    
    # Converte o campo Valor para float
    df['Valor'] = pd.to_numeric(df['Valor'])
    
    
    # Agrupamento, utilizando a sintaxe groupby, das vendas por vendedor, ordendo do maior para o menor com a função de sort_values
    vendas_por_vendedor = df.groupby("Vendedor")["Valor"].sum().sort_values(ascending=False)
    
    # Identificação do cliente da venda com maior valor, selecionando
    venda_maior_valor = df.loc[df["Valor"] == df["Valor"].max()]
    
    # Identificação do cliente da venda com menor valor
    venda_menor_valor = df.loc[df["Valor"] == df["Valor"].min()]
    
    # Cálculo do valor médio por tipo de venda
    valores_por_tipo = df.groupby("Tipo")["Valor"].mean()
    
    # Cálculo do número de vendas por cliente
    vendas_por_cliente = df.groupby("Cliente")["ID"].nunique()
    
    # Impressão dos resultados
    print("Venda com maior valor:")
    print({venda_maior_valor['Cliente'].values[0]}, "Valor:", {venda_maior_valor['Valor'].values[0]})
    print('\n')
    print("Venda com menor valor:")
    print({venda_menor_valor['Cliente'].values[0]}, "Valor:",{venda_menor_valor['Valor'].values[0]})
    print('\n')
    print("Valor médio por tipo de venda:")
    print(valores_por_tipo)
    print('\n')
    print("Número de vendas realizada por cliente:")
    print(vendas_por_cliente)

if __name__ == "__main__":
    main()
