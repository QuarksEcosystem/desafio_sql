-- Consulta para listar todas as vendas (ID), clientes e datas de venda no ano de 2020
SELECT ID, Cliente, `Data da Venda`
FROM DB_Teste
WHERE YEAR(`Data da Venda`) = 2020;

-- Consulta para construir uma tabela que avalia os resultados das vendas trimestralmente
SELECT YEAR(`Data da Venda`) AS Ano, 
       QUARTER(`Data da Venda`) AS Trimestre, 
       SUM(Valor) AS TotalVendas
FROM DB_Teste
GROUP BY YEAR(`Data da Venda`), QUARTER(`Data da Venda`);

-- Consulta para listar a equipe de cada vendedor
SELECT Vendedor, Equipe
FROM DB_Teste
GROUP BY Vendedor, Equipe;
