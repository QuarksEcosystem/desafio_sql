import streamlit as st
from service.connect import init_connection
from sql_consults.sql import delete_venda, fill_database
from Homepage import data
from service.connect import init_connection
from functions_sql import get_sales_2020, get_team, quarterly_sales
import pandas as pd
import matplotlib.pyplot as plt

conn = init_connection()
st.title("SQL scenarios")

# Limitar para executar apenas uma vez

#delete_venda(conn)
fill_database(data, conn)

# Listar todas as vendas (ID) e seus respectivos clientes apenas no ano de 2020
st.dataframe(get_sales_2020(conn))

# Listar a equipe de cada vendedor
st.dataframe(get_team(conn))

# Construir uma tabela que avalia trimestralmente o resultado de vendas e plote um gráfico deste histórico.

# Plotar um gráfico de barras
df = quarterly_sales(conn)
plt.figure(figsize=(10, 6))
for ano in df['ano'].unique():
    df_ano = df[df['ano'] == ano]
    plt.bar(df_ano['trimestre'], df_ano['valor'], label=str(ano))

plt.xlabel('Trimestre')
plt.ylabel('Valor de Vendas')
plt.title('Resultado de Vendas por Trimestre')
plt.legend()
st.pyplot(plt)
