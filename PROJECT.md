# Execução do Projeto

<p>Para realizar o projeto, escolhi utilizar o jupyter notebook, que se adequa bem às tarefas requeridas, pois já vem com a biblioteca
pandas instalada. A biblioteca pandas é uma ferramenta poderosa para a análise de arquivos csv e de arquivos com tabelas de dados no geral, pois permite que se extraia, trate e analise os dados de maneira bem intuitiva e com uma curva de aprendizado relativamente pequena.</p>
<p>Os arquivos do tipo .ipynb podem ser executados tanto a partir do Google Colab, que é análogo ao jupyter notebook, ou pelo próprio
jupyter notebook. Para acessar o colab basta usar o seguinte link: <mark>https://colab.google/</mark> -> Open Colab -> Upload -> selecionar o arquivo .ipynb para a execução</p>

### Instalação do Jupyter Notebook
<p>Caso escolha utilizar o jupyter notebook, basta seguir os passos descritos no seguinte link: <mark>https://jupyter.org/install</mark>. Neste caso, o pacote pandas não virá instalado por padrão. Para instalá-lo, basta seguir o passo a passo contido nesse link: <mark>https://pandas.pydata.org/docs/getting_started/install.html</mark> na seção <mark>"Installing from PyPI"</mark>. É possível também instalar o conda, que já vem com o jupyter notebook e o pandas. Para fazer isto basta seguir o passo a passo contido neste link: <mark>https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html</mark> para Windows<br> ou <mark>https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html</mark> para o Linux.</p>
<p>Uma vez que o Jupyter notebook estiver instalado, para executá-lo, basta abrir um terminal de comando e digitar 'jupyter notebook', em seguida ir até a pasta onde se encontra o arquivo .ipynb, abrir o arquivo e executar o código.</p>

# Explicação do projeto - Python

+ Primeiramente, abrimos o arquivos csv com a função read_csv. Numa análise prévia do arquivo, é possível ver que o separador utilizado é o ponto e vírgula ';', portanto, precisamos explicitar usando o parâmetro 'sep' na função que o separador não é a vírgula, que é o separador default.
+ É sempre aconselhável, quando trabalhando com um projeto com dados, realizar uma inspeção dos dados e tratar quaisquer problemas que possam estar contidos na base de dados, como colunas sem dados, colunas com nomes não intuitivos ou com tipos de dados não coerentes, assim como linhas duplicadas ou linhas vazias. É bom ressaltar que a exclusão ou não de uma linha ou coluna fica a critério da pessoa que está fazendo a análise, e talvez uma coluna sem dados, por exemplo, deva ser mantida paraque seja preenchida depois, caso isto faça sentido.
+ No código realizei as seguintes etapas de tratamento:
  1. exclusão de uma coluna que não continha nenhum dado e que não estava no arquivo csv original, a coluna 'Unnamed: 10';
  2. conversão do tipo da coluna 'Valor' de string para float, para que fosse possível realizar análises numéricas;
  3. Verifiquei a existência de uma linha com ID duplicada, mas que representa duas vendas diferentes. Decidi apenas guardar a ID em uma variável para se, caso alguma análise necessita-se deste campo, fosse possível usá-la para futuras verificações e que devidas correções fossem aplicadas.

### Análise
+ Na primeira parte da análise, apliquei a função de groupby('Vendedor') e sobre esta função apliquei sum('Valor'), desta forma cada vendedor fica associado à soma de todas suas vendas. Coloquei o resultado numa tabela chamada resumo_vendas. Sobre esta tabela apliquei a função de sort_values no campo valor, de forma descrescente com o parâmetro 'ascending=False' e renomeei o campo 'Valor' para 'Valor por Vendedor' para melhorar o entendimento da tabela.
+ Na segunda parte, para encontrar os clientes com as vendas de menor e maior valor, utilizei a função loc sobre o ids de valores máximo e mínimo, retornando o valor contido na coluna cliente. Isto retorna os clientes que queríamos identificar.
+ Na terceira parte, agrupei a tabela no campo 'Tipo' e apliquei a média sobre o campo 'Valor', isto devolve a média associada a cada tipo de venda existente na base de dados. Este resultado foi guardado numa nova tabela denominada 'valor_medio_tipo'. Em seguida arredondei o campo valor para duas casas decimais, para fazer sentido com a notação de valor monetário e melhorar a legibilidade. Também mudei a coluna 'Valor' para 'Valor Medio por Tipo' para melhorar o entendimento do que a tabela significa.
+ Na última parte do código, apliquei a função value_counts no campo cliente. Essa ação retorna o número de ocorrências associado a cada cliente presente na base de dados. Neste caso as ocorrências de cada cliente representam uma venda cada, portanto, basta renomear as colunas para 'Número de Vendas'.


# Desafio SQL
<p>A primeira parte do desafio envolveu a criação de um banco de dados relacional a partir das entidades contidas no arquivo csv. O diagrama de relações que eu criei está contido no arquivo pdf '<mark>desafio_sql_triggoai</mark>' presente neste repositório. Minha ideia foi de criar tabelas apenas com as entidades mais importantes, ou seja, a Venda, o Cliente, o Vendedor e a Equipe. Acredito que este banco é capaz de trazer todas as principais relações entre as entidades mantendo uma simplicidade e manutenabilidade. A seguir explico as cardinalidades entre cada entidade do banco.</p>

### Cliente <-> Venda
<p>Como visto no diagrama, a cardinalidade da relação é do tipo 1 Cliente para 0 a n Vendas, pois um cliente pode ainda não estar associado a uma venda ou ter n vendas a ele associadas.</p>

### Venda <-> Vendedor
<p>Assim como no caso Cliente-Venda, a cardinalidade escolhida para a relação Venda-Vendedor foi 1 Vendedor para 0 a n Vendas. A escolha se justifica pois um vendedor pode ainda não ter realizado uma venda, ou já realizado n vendas.</p>

### Vendedor <-> Equipe
<p>Finalmente, para o caso vendedor-equipe, foi escolhida a cardinalidade de n vendedores para 1 ou nenhuma equipe. Esta escolha se dá pois uma equipe precisa ter pelo menos n vendedores para ser considerada uma equipe, e um vendedor pode ou não ser parte de uma equipe, mas apenas uma equipe.</p>

## Queries MySQL
1. A primeira query faz seleciona as ids na tabela venda e os nomes dos clientes na tabela de clientes, fazendo um inner join entre as tabelas, ou seja, pegando apenas correpondências que tenham um match em ambas as tabelas Venda e Clientes, e aplicando um filtro de forma que apenas as vendas realizadas no ano de 2020 sejam mostradas.
2. A segunda query seleciona os ids dos vendedores, seus nomes e o nome da equipe na tabela Equipe. Neste Caso um left join é aplicado, pois, como explicado anteriormente, um vendedor pode ou não ter uma equipe, o left join irá unir os vendedores e as equipes mesmo que alguns vendedores não tenham equipe.

## Tabela Resultado Trimestral
<p>A tabela ResultadosTrimestrais foi criada com os seguintes campos: id (primary key), ano, trimestre e valorTotal. Para preencher esta tabela, a query utilizada, também presente no arquivo pdf, tem a seguinte lógica: seleciona o ano da venda, o trimestre da venda e a soma dos valores aplicando o filtro onde escolhemos quais são o ano e o trimestre da venda.</p>

## Gráfico Resultado Trimestral
1. Utilizando o arquivo csv, podemos criar o gráfico proposto. Primeiramente criamos uma coluna 'Trimeste' na nossa base de dados, associando a cada venda o seu trimestre em um dado ano.
2. Podemos então criar uma tabela que agrupa as vendas por trimestre e soma seus valores.
3. Finalmente, usando a biblioteca matplotlib, podemos plotar o gráfico do valor de vendas em função de cada trimestre