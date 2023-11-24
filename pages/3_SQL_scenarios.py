import streamlit as st
from service.connect import init_connection
from sql_consults.sql import executar_consulta_sql, executar_instrucao_sql
from Homepage import data

st.title("SQL scenarios")

conn = init_connection()

nomes_clientes_unicos = data['Cliente'].unique()
st.dataframe(nomes_clientes_unicos)


if conn:
    st.title("Aplicativo Streamlit com PostgreSQL")

    for nome_cliente in nomes_clientes_unicos:
        query_insercao = f"INSERT INTO CLIENTE (Nome) VALUES ('{nome_cliente}') ON CONFLICT (Nome) DO NOTHING;"
        executar_instrucao_sql(query_insercao, conn)

    st.success("Nomes únicos inseridos na tabela de clientes.")
else:
    st.warning("A conexão com o banco de dados não foi bem-sucedida.")



if conn:    
    st.title("Aplicativo Streamlit com PostgreSQL")

    # Exemplo de consulta SQL
    query = "SELECT * FROM CLIENTE;"

    # Executar a consulta e exibir os resultados
    df_resultado = executar_consulta_sql(query, conn)

    if df_resultado is not None:
        st.write("Resultados da consulta:")
        st.write(df_resultado)
else:
    st.warning("A conexão com o banco de dados não foi bem-sucedida.")