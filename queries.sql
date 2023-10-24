--postgresql

--Vendas e clientes no ano de 2020
SELECT id_venda
FROM vendas v
LEFT JOIN clientes c
ON v.id_cliente = c.id_cliente
WHERE extract('year' from date(data_venda)) = 2020
;

--Listagem da equipe de cada vendedor
SELECT DISTINCT v2.vendedor, e.equipe
FROM vendas v1
LEFT JOIN vendedor v2
ON v1.id_vendedor = v2.id_vendedor
LEFT JOIN equipe e
ON v1.id_equipe = e.id_equipe
;

--Ticket médio por trimestre
SELECT SUM(valor) / COUNT(id_venda) AS ticket_medio, extract('year' from date(data_venda)) as ano, extract('month' from date(data_venda)) as mes
FROM vendas
GROUP BY ano, mes
;


