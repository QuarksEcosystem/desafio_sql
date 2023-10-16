Desafio triggo.ai

**PYTHON**

Para começar a trabalhar com Python, você precisa instalar o interpretador na sua máquina. Você pode fazer isso baixando o instalador do site oficial do Python.

Após baixar o instalador, execute-o e siga as instruções na tela. Após a instalação, você pode verificar se o Python foi instalado corretamente digitando o seguinte comando em um terminal:

```
python --version
```

**Instalação da biblioteca Pandas**

A biblioteca Pandas é uma biblioteca de análise de dados para Python. Para instalá-la, você pode usar o seguinte comando em um terminal:

```
pip install pandas
```

**Instalação do MySQL**

O MySQL é um sistema de gerenciamento de banco de dados relacional. Para instalá-lo, você pode baixar o instalador do site oficial do MySQL.

Após baixar o instalador, execute-o e siga as instruções na tela. Após a instalação, você pode iniciar o MySQL digitando o seguinte comando em um terminal:

```
sudo mysql
```

**Execução dos códigos Python e SQL**

Para executar os códigos Python e SQL, você precisa salvá-los em arquivos com as extensões ".py" e ".sql", respectivamente.

**Código Python**

O código Python lê um arquivo CSV chamado "DB_Teste.csv" e realiza as seguintes operações:

* Remove os pontos e vírgulas do campo "Valor".
* Converte o campo "Valor" para float.
* Agrupa as vendas por vendedor, ordenando do maior para o menor.
* Identifica o cliente da venda com maior valor.
* Identifica o cliente da venda com menor valor.
* Calcula o valor médio por tipo de venda.
* Calcula o número de vendas por cliente.

**Código SQL**

O código SQL cria as seguintes tabelas no banco de dados:

* `cliente`: tabela para armazenar os dados dos clientes.
* `vendedor`: tabela para armazenar os dados dos vendedores.
* `equipe`: tabela para armazenar os dados das equipes.
* `tipo`: tabela para armazenar os dados dos tipos de venda.
* `categoria`: tabela para armazenar os dados das categorias de venda.
* `regional`: tabela para armazenar os dados das regiões.
* `venda`: tabela para armazenar os dados das vendas.

O código SQL também realiza as seguintes operações:

* Adiciona as chaves estrangeiras às tabelas.
* Realiza uma consulta para selecionar todas as vendas realizadas em 2020.
* Realiza uma consulta para selecionar todos os vendedores e equipes associados a cada venda.
* Realiza uma consulta para selecionar o valor total de vendas por ano e trimestre.

**Explicação dos códigos**

**Código Python**

O código Python utiliza a biblioteca Pandas para realizar as operações. A biblioteca Pandas é uma biblioteca de análise de dados para Python.

Aqui estão os detalhes de cada operação realizada pelo código Python:

* A função `read_csv()` lê o arquivo CSV e cria um DataFrame.
* A função `str.replace()` remove os pontos e vírgulas do campo "Valor".
* A função `pd.to_numeric()` converte o campo "Valor" para float.
* A função `groupby()` agrupa as vendas por vendedor.
* A função `sort_values()` ordena os grupos do maior para o menor.
* A função `loc()` seleciona a linha com o valor máximo do campo "Valor".
* A função `loc()` seleciona a linha com o valor mínimo do campo "Valor".
* A função `groupby()` agrupa as vendas por tipo de venda

Por fim, para a construção do gráfico, utilizaremos a função de `sum` e `quarter` para retornar a soma do valor das vendas, quebrando por trimestre. Depois de extrair as informações pelo SQL, montaremos, em python, a construção do gráfico através da biblioteca `matplotlib`, que deverá ser instalada e lida da mesma maneira e, após isso, o código deverá ser executado.

Esse código cria um gráfico de linha para visualizar a evolução do valor total de vendas por ano.

A função `import matplotlib.pyplot as plt` importa a biblioteca Matplotlib, que é usada para criar gráficos.
A função `read_sql_query()` lê os dados do banco de dados MySQL.
A função `plot()` cria o gráfico de linha.
A função `xlabel()` adiciona um rótulo ao eixo x.
A função `ylabel()` adiciona um rótulo ao eixo y.
A função `show()` exibe o gráfico.

Após isso, o gráfico será gerando dentro do próprio python, facilitando a visualização dos números e indicadores, para que seja gerado os insights necessários. 
