-- ========================
-- BANCO DE DADOS
-- ========================
CREATE DATABASE nome;
USE nome;
DROP DATABASE nome;

-- ========================
-- SELECT (Consulta)
-- ========================
SELECT coluna1, coluna2
FROM tabela;

SELECT * FROM tabela;

-- ========================
-- FILTROS (WHERE)
-- ========================
SELECT * FROM tabela
WHERE coluna = 'valor';

-- Operadores
-- =, >, <, >=, <=, <>
-- AND / OR / NOT

-- Exemplo
SELECT * FROM Customers
WHERE Country = 'Brazil' AND City = 'Rio de Janeiro';

-- ========================
-- ORDENAÇÃO
-- ========================
SELECT * FROM tabela
ORDER BY coluna ASC;  -- Crescente
ORDER BY coluna DESC; -- Decrescente

-- ========================
-- INSERÇÃO
-- ========================
INSERT INTO tabela (col1, col2)
VALUES ('valor1', 'valor2');

-- Múltiplos
INSERT INTO tabela (col1, col2)
VALUES
('v1','v2'),
('v3','v4');

-- ========================
-- UPDATE
-- ========================
UPDATE tabela
SET coluna = 'novo_valor'
WHERE condição;

-- ========================
-- DELETE
-- ========================
DELETE FROM tabela WHERE condição;
DELETE FROM tabela; -- tudo

-- ========================
-- NULL
-- ========================
SELECT * FROM tabela WHERE coluna IS NULL;
SELECT * FROM tabela WHERE coluna IS NOT NULL;

-- ========================
-- LIMITAR RESULTADOS
-- ========================
SELECT TOP 3 * FROM tabela;

-- ========================
-- FUNÇÕES AGREGADAS
-- ========================
SELECT MIN(coluna) FROM tabela;
SELECT MAX(coluna) FROM tabela;
SELECT COUNT(*) FROM tabela;
SELECT SUM(coluna) FROM tabela;
SELECT AVG(coluna) FROM tabela;

-- Com GROUP BY
SELECT coluna, COUNT(*)
FROM tabela
GROUP BY coluna;

-- ========================
-- LIKE (Busca com padrão)
-- ========================
SELECT * FROM tabela WHERE nome LIKE 'A%';   -- começa com A
SELECT * FROM tabela WHERE nome LIKE '%A';   -- termina com A
SELECT * FROM tabela WHERE nome LIKE '%A%';  -- contém A

-- ========================
-- IN
-- ========================
SELECT * FROM tabela
WHERE coluna IN ('A', 'B', 'C');

-- ========================
-- BETWEEN
-- ========================
SELECT * FROM tabela
WHERE valor BETWEEN 10 AND 20;

-- ========================
-- ALIAS
-- ========================
SELECT coluna AS apelido
FROM tabela;

-- ========================
-- JOIN (Junções)
-- ========================
-- INNER JOIN
SELECT *
FROM tabela1
INNER JOIN tabela2
ON tabela1.id = tabela2.id;

-- LEFT JOIN
SELECT *
FROM tabela1
LEFT JOIN tabela2
ON tabela1.id = tabela2.id;

-- RIGHT JOIN
SELECT *
FROM tabela1
RIGHT JOIN tabela2
ON tabela1.id = tabela2.id;

-- ========================
-- UNION
-- ========================
SELECT coluna FROM tabela1
UNION
SELECT coluna FROM tabela2;

-- UNION ALL (inclui duplicados)
SELECT coluna FROM tabela1
UNION ALL
SELECT coluna FROM tabela2;
