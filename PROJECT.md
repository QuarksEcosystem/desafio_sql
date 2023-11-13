# Estágio Desenvolvedor SQL
## TRECHO: Python - Status: Concluído  
## Implemente em python um programa que tenha como entradas o arquivo CSV e realize as seguintes tarefas:

	Construa uma tabela auxiliar que sumarize o valor vendido por cada vendedor, ordenando do maior para o menor;

	Imprima e identifica qual foi o cliente responsável pela venda com maior valor e com menor valor;

	Imprima valor médio por Tipo de venda (Serviços, Licenciamento, Produtos)

	Imprima o número de vendas realizada por cliente;
  
## Tabela de conteúdos
<!--ts-->
   * [Sobre](#Sobre)
   * [Tabela de Conteudo](#tabela-de-conteudo)
   * [Instalação](#instalacao)
   * [Tecnologias](#tecnologias)
<!--te-->
<a id="Sobre"></a>
## Sobre 
Implementação da parte python do desafio proposto, modelado no Jupyter notebook, de forma que não existe necessidade de instalação de interpretadores ou bibliotecas.
<a id="Instalacao"></a>

## Instalação
Esse projeto pode ser executado de forma direta clicando no botão abaixo: <p><a href="https://colab.research.google.com/github/joaovrmdev/desafio_sql/blob/main/Desafio.ipynb"><img data-canonical-src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" src="https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667"></a></p>

<a id="tecnologias"></a>
## 🛠 Tecnologias
As seguintes ferramentas foram usadas na construção do projeto:</br>
- Linguagem:
 -  [Jupyter notebook](https://jupyter.org/)</br>
- Bibliotecas:
 -  [Pandas](https://pandas.pydata.org/)



## TRECHO: SQL - Status: Concluído  


### Construir o Modelo de Relacionamento com as Categorias Utilizadas em Todos os Campos do Arquivo CSV

 -  [Imagem](https://drive.google.com/drive/folders/1okN5hH5_StBtTQdpRW099liRLUo_naWu?usp=sharing)


```sql
-- Criar tabela para armazenar as informações
CREATE TABLE Vendas (
    Cliente VARCHAR2(255),
    ID VARCHAR2(10),
    Tipo VARCHAR2(255),
    Data_da_Venda DATE,
    Categoria VARCHAR2(255),
    Vendedor VARCHAR2(255),
    Regional VARCHAR2(255),
    Duracao_do_Contrato_Meses NUMBER,
    Equipe VARCHAR2(255),
    Valor NUMBER
);

-- Para carregar os dados do CSV, podemos usar o SQL*Loader ou funções INSERT.

-- Adicionar índices conforme necessário para otimizar consultas.
```

### Listar Todas as Vendas (ID) e Seus Respectivos Clientes Apenas no Ano de 2020

```sql
SELECT ID, Cliente
FROM Vendas
WHERE EXTRACT(YEAR FROM Data_da_Venda) = 2020;
```

### Listar a Equipe de Cada Vendedor

```sql
SELECT DISTINCT Vendedor, Equipe
FROM Vendas;
```

### Construir uma Tabela que Avalia Trimestralmente o Resultado de Vendas e Plote um Gráfico Deste Histórico

Para criar uma tabela que avalia trimestralmente o resultado de vendas, você pode usar a função `TRUNC` para agrupar por trimestre. No Oracle, você pode usar o seguinte código:

```sql
CREATE TABLE Resultado_Trimestral AS
SELECT 
    TRUNC(Data_da_Venda, 'Q') AS Trimestre,
    SUM(Valor) AS Total_Vendas
FROM Vendas
GROUP BY TRUNC(Data_da_Venda, 'Q')
ORDER BY Trimestre;

-- Para plotar um gráfico, podemos usar ferramentas como Oracle SQL Developer.
```

Se precisar de mais esclarecimentos ou tiver dúvidas específicas, estou à disposição.


### Autor
<a>
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/83680277?v=4" width="100px;" alt="Imagem do autor"/>
 <sub><b>João vitor</b></sub></a> <a href="https://www.linkedin.com/in/joaovrm/" title="LinkedIn">🚀</a>

Feito com dedicação e curiosidade.

![Github Badge](https://img.shields.io/github/followers/joaovrmdev?style=social)
[![Gmail Badge](https://img.shields.io/badge/-joao.mata1111@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:joao.mata1111@gmail.com)](mailto:joao.mata1111@gmail.com)
