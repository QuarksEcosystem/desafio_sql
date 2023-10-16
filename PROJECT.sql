CREATE TABLE cliente (
  id integer PRIMARY KEY,
  nome varchar(255)
);

CREATE TABLE vendedor (
  id integer PRIMARY KEY,
  nome varchar(255)
);

CREATE TABLE equipe (
  id integer PRIMARY KEY,
  nome varchar(255)
);

CREATE TABLE tipo (
  id integer PRIMARY KEY,
  nome varchar(255)
);

CREATE TABLE categoria (
  id integer PRIMARY KEY,
  nome varchar(255)
);

CREATE TABLE regional (
  id integer PRIMARY KEY,
  nome varchar(255)
);

CREATE TABLE venda (
  id varchar(255) PRIMARY KEY,
  cliente_id integer,
  tipo_id integer,
  equipe_id integer,
  vendedor_id integer,
  categoria_id integer,
  regional_id integer,
  duracao_contrato_meses integer,
  data date,
  valor decimal
);

ALTER TABLE venda ADD FOREIGN KEY (cliente_id) REFERENCES cliente (id);

ALTER TABLE venda ADD FOREIGN KEY (vendedor_id) REFERENCES vendedor (id);

ALTER TABLE venda ADD FOREIGN KEY (equipe_id) REFERENCES equipe (id);

ALTER TABLE venda ADD FOREIGN KEY (tipo_id) REFERENCES tipo (id);

ALTER TABLE venda ADD FOREIGN KEY (regional_id) REFERENCES regional (id);

ALTER TABLE venda ADD FOREIGN KEY (categoria_id) REFERENCES categoria (id);
SELECT
    venda.id,
    cliente.nome
FROM
    venda
INNER JOIN
    cliente on cliente.id = venda.cliente_id
WHERE
    YEAR(venda.data) = 2020;


SELECT
    vendedor.nome,
    equipe.nome
FROM
    venda
INNER JOIN
    vendedor on vendedor.id = venda.vendedor_id
INNER JOIN
    equipe on equipe.id = venda.equipe_id
GROUP BY
    vendedor.nome,
    equipe.nome;



SELECT
  EXTRACT(YEAR FROM data) AS ano,
  EXTRACT(QUARTER FROM data) AS trimestre,
  SUM(valor) AS valor
FROM   venda
GROUP BY   ano,   trimestre;
