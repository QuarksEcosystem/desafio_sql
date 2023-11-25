import streamlit as st
import pandas as pd


def execute_sql_query(query, conn):
    """_summary_ : Query the database and return a dataframe

    Args:
        query (_type_): String with the SQL query
        conn (_type_): psycopg2.connection

    Returns:
        _type_: None
    """
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        st.error(f"Erro ao executar a consulta: {e}")
        return None


def execute_sql_instruction(query, conn):
    """_summary_ : Execute a SQL query

    Args:
        query (_type_): String with the SQL query
        conn (_type_): psycopg2.connection
    """
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            conn.commit()
    except Exception as e:
        st.error(f"Erro ao executar a instrução SQL: {e}")


def fill_database(data, conn):
    """_summary_ : Fill the database with the data from the dataframe

    Args:
        data (_type_): Pandas dataframe
        conn (_type_): psycopg2.connection
    """
    client_names = data['Cliente'].unique()
    sellers_team = data.groupby('Vendedor')['Equipe'].agg(lambda x: ', '.join(x.unique())).reset_index() 

    if conn:
        query_check_empty = "SELECT COUNT(*) FROM VENDA;"
        result_empty_check = execute_sql_query(query_check_empty, conn)

        if result_empty_check is not None and result_empty_check.iloc[0, 0] == 0:
            st.warning("A tabela 'VENDA' está vazia. Inserindo dados.")

            for client in client_names:
                query_client = f"INSERT INTO CLIENTE (Nome) VALUES ('{client}') ON CONFLICT (Nome) DO NOTHING;"
                execute_sql_instruction(query_client, conn)
            
            for index, row in sellers_team.iterrows():
                seller = row['Vendedor']
                team = row['Equipe']
                
                query_seller = f"INSERT INTO VENDEDOR (Nome, Timee) VALUES ('{seller}', '{team}') ON CONFLICT (Nome) DO NOTHING;"
                execute_sql_instruction(query_seller, conn)
            
            for index, row in data.iterrows():
                nome_cliente = row['Cliente']
                id_venda = row['ID']
                tipo = row['Tipo']
                data_da_venda = row['Data da Venda']
                categoria = row['Categoria']
                nome_vendedor = row['Vendedor']
                regional = row['Regional']
                duracao_do_contrato = row['Duração do Contrato (Meses)']
                equipe = row['Equipe']
                valor = row['Valor']

                query_insercao_venda = f"INSERT INTO VENDA (Nome_cliente, ID, Tipo, DataDaVenda, Categoria, Nome_vendedor, Regional, DuracaoDoContrato, Equipe, Valor) " \
                                    f"VALUES ('{nome_cliente}', '{id_venda}', '{tipo}', '{data_da_venda}', '{categoria}', '{nome_vendedor}', '{regional}', {duracao_do_contrato}, '{equipe}', {valor});"
                
                execute_sql_instruction(query_insercao_venda, conn)

            st.success("Dados inseridos com sucesso.")
    else:
        st.warning("A conexão com o banco de dados não foi bem-sucedida.")