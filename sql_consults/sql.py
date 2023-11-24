import streamlit as st
import pandas as pd


def executar_consulta_sql(query, conn):
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        st.error(f"Erro ao executar a consulta: {e}")
        return None


def executar_instrucao_sql(query, conn):
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
    except Exception as e:
        st.error(f"Erro ao executar a instrução SQL: {e}")