# PROJETO SQL TRIGGO.AI

Repositório contendo o código do desafio e explicações de como rodar.
Também contenco algumas explicações do código.

## Instalação do pip, criação de um venv e instalação dos requirements

Foi escolhido o uso do Streamlit onde podemos criar sites/dashboards interativas de maneira mais fácil utilizando python, ideal para unir a apresentação dos dados com alguns modelos de ML ou AI por exemplo.

- Instale o "pip":
```shell
sudo apt-get install python3-pip
```
- Entre na pasta raiz do projeto:
```shell
cd desafio_sql_streamlit
```
- Cria um ambiente virtual (Este passo é importante pois o streamlit recomenda o uso de um venv):
```shell
python -m venv .venv
```
- Instalar as dependências por meio do arquivo requirements.txt, o -r serve para ler de maneira recursiva o documento assim instalando todas as dependências contidas no arquivo:
```shell
pip install -r requirements.txt
```

## Configurando a conexão ao servidor do PostgreSQL

Na conexão com o PostgreSQL é necessário a instalação do do mesmo no computador, já que o database é tratado como "localhost".

- Abra o arquivo connect.py, aqui está indicando o vim para ser aberto, mas qualquer editor de texto pode ser utilizado:
```shell
cd services
vim connect.py
```
O Arquivo terá as seguintes informações, deve-se realizar modificações na configuração da conexão:
```shell
import psycopg2

def init_connection():
    """_summary_ : Connect to PostgreSQL database

    Returns:
        _type_: psycopg2.connection
    """
    conn = psycopg2.connect(
        host="localhost",
        database="DB_teste",
        user="postgres",
        password="123456",
        port=5432
    )
    return conn
```

# Execução do código
- Para executar o código deve-se rodar o arquivo Homepage.py, que neste caso funcionará como se fosse uma função main.
```shell
streamlit run Homepage.py
```


