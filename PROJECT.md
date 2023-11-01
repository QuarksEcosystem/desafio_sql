# Projeto de Análise de Dados de Vendas

Este projeto visa analisar um arquivo de dados CSV 'DB_Teste.csv' contendo informações de vendas. O script em Python fornecido realiza uma análise básica dos dados e apresenta diversos insights sobre as vendas, vendedores, clientes e tipos de venda.

## Como Executar o Projeto

### Requisitos:
- Python instalado (versão utilizada: 3.x)
- Arquivo 'DB_Teste.csv'

### Passos:
1. Baixe o arquivo 'DB_Teste.csv' e salve-o no mesmo diretório onde o script em Python será executado.

2. Execute o script Python fornecido em um ambiente que tenha suporte à linguagem Python. Isso pode ser feito abrindo um terminal ou prompt de comando, navegando até o diretório onde o arquivo 'PROJECT.md' e o script Python estão localizados e executando o comando:

   ```bash
   python python_db.py

   Detalhes do Script Python
   
## Detalhes do Script Python

O script em Python realiza as seguintes operações:

1. **Inicialização de Variáveis:** Inicializa variáveis para armazenar informações sobre vendedores, clientes e tipos de vendas.

2. **Leitura do Arquivo CSV:** Abre o arquivo 'DB_Teste.csv' e lê as linhas do arquivo para analisar os dados contidos.

3. **Cálculo de Métricas:** Realiza o cálculo de diversas métricas, tais como:
    - Vendasto totais por vendedor.
    - Identificação do cliente com o maior e menor volume de vendas.
    - Cálculo da média de vendas por tipo.
    - Contagem do número de vendas por cliente.

4. **Apresentação dos Resultados:** Exibe os resultados da análise no console.



# Projeto de Análise de Dados - Instruções e Consultas SQL

Este projeto visa a análise de um banco de dados usando consultas SQL para extrair informações específicas. As consultas fornecidas atendem a diferentes requisitos de análise.

## Como Executar o Projeto

1. **Preparação do Ambiente**:
   - Configure um banco de dados relacional (por exemplo, MySQL, SQL Server, etc.).
   - Importe os dados do arquivo 'DB_Teste.csv' para o seu banco de dados.

2. **Execução das Consultas SQL**:
   Utilize o seu cliente SQL preferido (como MySQL Workbench, SQL Server Management Studio, etc.) e execute as consultas a seguir:

### Consulta 1: Listar todas as vendas (ID), clientes e datas de venda no ano de 2020

```sql
SELECT ID, Cliente, `Data da Venda`
FROM DB_Teste
WHERE YEAR(`Data da Venda`) = 2020;

```
### Consulta 2: Construir uma tabela que avalia os resultados das vendas trimestralmente

```sql
SELECT YEAR(`Data da Venda`) AS Ano, 
       QUARTER(`Data da Venda`) AS Trimestre, 
       SUM(Valor) AS TotalVendas
FROM DB_Teste
GROUP BY YEAR(`Data da Venda`), QUARTER(`Data da Venda`);
```

### Consulta 3: Listar a equipe de cada vendedor

```sql
SELECT Vendedor, Equipe
FROM DB_Teste
GROUP BY Vendedor, Equipe;

```

### Considerações Finais - Programa em Python

O programa em Python apresenta uma análise básica dos dados contidos no arquivo 'DB_Teste.csv'. Ele calcula métricas como vendas totais por vendedor, identifica o cliente com o maior e menor volume de vendas, calcula a média de vendas por tipo e conta o número de vendas por cliente. Essas métricas fornecem uma visão inicial dos dados, podendo ser ampliadas ou ajustadas para análises mais detalhadas ou específicas, conforme as necessidades do projeto.

### Considerações Finais - Consultas SQL

As consultas SQL fornecidas visam atender a diferentes requisitos de análise sobre o banco de dados 'DB_Teste'. A primeira consulta lista todas as vendas (ID), clientes e datas de venda no ano de 2020. A segunda constrói uma tabela que avalia os resultados das vendas trimestralmente, apresentando o total de vendas por trimestre. Por fim, a terceira consulta lista a equipe de cada vendedor.

Essas consultas oferecem informações específicas a partir do banco de dados, possibilitando a análise e obtenção de insights relevantes sobre as vendas registradas.

Caso haja necessidade de ampliação, modificação ou suporte adicional em relação ao programa em Python ou às consultas SQL, estou à disposição para fornecer orientação e suporte.

