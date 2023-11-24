import streamlit as st
from Homepage import data
from functions_tasks import best_seller, best_client, mean_type_sale, sale_per_client

st.title("CSV Tasks")
# Transform values from 'Valor' column to float

data_best_seller = best_seller(data)

# Imprima e identifica qual foi o cliente responsável pela venda com maior valor e com menor valor;
data_best_cliente = best_client(data)

# Imprima valor médio por Tipo de venda (Serviços, Licenciamento, Produtos);
data_mean = mean_type_sale(data)

# Imprima o número de vendas por cliente;
data_sale_per_client = sale_per_client(data)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Vendas por vendedor")
    st.dataframe(data_best_seller, width=600)

with col2:
    st.subheader("Clientes responsáveis pela maior e menor venda")
    st.dataframe(data_best_cliente, hide_index=True, width=600)

col3, col4 = st.columns(2)

with col3:
    st.subheader("Valor Médio por Tipo de Venda")
    st.dataframe(data_mean, hide_index=True, width=600)

with col4:
    st.subheader("Número de Vendas por Cliente")
    st.dataframe(data_sale_per_client,width=600)



