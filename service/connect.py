import psycopg2

def init_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="DB_teste",
        user="postgres",
        password="123456",
        port=5432
    )
    return conn
