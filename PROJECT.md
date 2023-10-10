### Como executar o arquivo .pynb

Para executar o arquivo .pynb pode se usar o serviço oferecido pela Google, o Google Colab, em que deve-se fazer o upload do arquivo DesafioPython.pynb (Arquivo -> Fazer upload de notebook) e ao abri-lo, deve-se fazer o upload do arquivo DB_Teste.csv (Clicar no ícone de pasta do lado esquerdo da interface e depois clicar com o botão direito na área vazia e clicar em upload).
Como alternativa, pode-se utilizar o pacote Anaconda do Python para abrir o notebook, certificando-se que está instalado a biblioteca Pandas e que o arquivo .csv esteja no mesmo local do arquivo .pynb.
Também é possível executa-lo de forma semelhante utilizando o VSCode e as extensões do Jupyter e do Python.

### Tarefas executadas

O primeiro passo foi importar a biblioteca pandas do Python, que servirá de base para os objetivos propostos, e carregar nossos dados .csv com a função read_csv do pandas.

Após isso, foi feita uma análise preliminar da natureza dos nossos dados com as funções .info() e .sample(), que foi constatada a presença de uma coluna com valores nulos, que foi removida logo em seguida com a função drop.

Também foi feita uma verificação na coluna ID sobre a presença de valores duplos com a função value_counts(), afim de garantir que cada dado da nossa tabela seja única, e constatou-se a presença de um ID com valor duplicado, que numa situação real seria interessante conversar com o cliente que nos forneceu os dados sobre a natureza desse valor e fazer o tratamento se fosse necessário. 

Além disso, foi feita uma análise do intervalo de tempo da coluna 'Data da Venda' com as funções min() e max(), afim de garantir que os nossos dados estão dentro do período informado.

E para finalizar a parte tratamento de dados, foi feita a conversão da coluna 'Valor', que é do tipo object para um tipo numérico para que seja possível realizar as tarefas propostas, para isso, foi usado a função replace() para remover o símbolo de Real, do ponto e a alteração do símbolo da casa decimal. Após isso, incluímos esses valores convertidos como uma nova coluna 'Valores' em nossa base de dados.

Para construir a tabela auxiliar que sumariza os valores vendidos pelos vendedores, pegamos as colunas 'Vendedor' e 'Valores' da base de dados original, aplicando um groupby em 'Vendedor' e realizando um sum() em 'Valores', após isso, ordenamos os valores dessa somatória em ordem decrescente com sort_values() com o atributo ascending=False.

Para identificar os clientes com a venda de maior e menor valor, foi utilizado a função idxmax() e idxmin() respectivamente dentro da função .loc(), o que nos retorna a linha completa dos dados, o que permitiu encontrar os respectivos clientes.

Para encontrar o valor médio por tipo de venda, foi usada as colunas 'Tipo' e 'Valores' da base de dados original, aplicando um groupby em 'Tipo' e realizando um mean() em 'Valores'.

Por fim, para obter o número de vendas realizadas por cada cliente, foi utilizada a função value_counts() na coluna 'Cliente', em que essa função nos retorna o número de vezes que cada cliente apareceu em nossos dados.