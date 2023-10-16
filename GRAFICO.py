import matplotlib.pyplot as plt

# Leitura dos dados
dados = pd.read_sql_query(query, conexao)

# Criação do gráfico
plt.plot(dados['ano'], dados['valor_total'])
plt.xlabel('Ano')
plt.ylabel('Valor total (R$)')
plt.show()
