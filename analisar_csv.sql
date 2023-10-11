SELECT Venda.VendaID, Cliente.NomeCliente
FROM Venda 
JOIN Cliente ON Venda.ClienteID = Cliente.ClienteID
WHERE YEAR(Venda.DataVenda) = 2020;
SELECT Vendedor.NomeVendedor, Vendedor.Equipe
FROM Vendedor;
SELECT 
  QUARTER(Venda.DataVenda) AS Trimestre,
  YEAR(Venda.DataVenda) AS Ano,
  SUM(Valor) AS TotalVendas
FROM Venda
GROUP BY YEAR(Venda.DataVenda), QUARTER(Venda.DataVenda)
ORDER BY Ano, Trimestre;
