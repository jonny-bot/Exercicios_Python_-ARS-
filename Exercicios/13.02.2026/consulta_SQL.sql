-- SQL DATABASE

-- Comentarios em linha

/* Comentarios
em varias Linhas */

-- Criação do Banco de Dados
CREATE DATABASE nome_do_banco;

-- Selecionar o Banco de Dados
USE nome_do_banco;

-- Excluir Banco de Dados
DROP DATABASE nome_do_banco;

/* SELECT */
-- Seleção (selciona todas as colunas)
SELECT coluna1, coluna2, ...
FROM nome_tabela;

-- Seleção (seleciona coluna especificas)
SELECT coluna1, coluna2, ...
FROM nome_da_tabela;

/* WHERE */
SELECT coluna1, coluna2, ...
FROM nome_tabela
WHERE coluna = 'dado_coluna';
-- where id_cliente = 1 | where nome_cliente = 'joao'

/* ORDER BY */
SELECT coluna1, coluna2, ...
FROM nome_tabela;
ORDER BY coluna1, coluna2, ... ASC|DESC; 
-- DESC: Ordem Decresente | ASC: Ordem Cresente

/* AND */
SELECT coluna1, coluna2, ...
FROM nome_tabela
WHERE condição1 AND condição2 AND condição3;

-- 	EXEMPLOS:

	SELECT * FROM Customers
	WHERE Country = 'Brazil'
	AND City = 'Rio de Janeiro'
	AND CustomerID > 50;

/* OR */
SELECT coluna1, coluna2, ...
FROM nome_tabela
WHERE condição1 OR condição2 OR condição3;

-- 	EXEMPLOS:
  
	SELECT * FROM Customers
	WHERE City = 'Berlin' OR CustomerName LIKE 'G%' OR Country = 'Norway';

/* NOT */
SELECT coluna1, coluna2, ...
FROM nome_tabela
WHERE NOT condição;

-- 	EXEMPLOS:

	-- NOT LIKE
	-- Selecione os clientes cujos nomes não começam com a letra 'A':
	SELECT * FROM Customers
	WHERE CustomerName NOT LIKE 'A%';
	
	-- NOT BETWEEN
	-- Selecione os clientes cujo ID não esteja entre 10 e 60:
	SELECT * FROM Customers
	WHERE CustomerID NOT BETWEEN 10 AND 60;
	
	-- NOT IN
	-- Selecione clientes que não sejam de Paris ou Londres:
	SELECT * FROM Customers
	WHERE City NOT IN ('Paris', 'London');
	
	-- NOT (Maior que)
	-- Selecione os clientes com um CustomerId não superior a 50:
	SELECT * FROM Customers
	WHERE NOT CustomerID > 50;
	
	-- NOT (Menor que)
	-- Selecione clientes com um ID de cliente igual ou superior a 50:
	SELECT * FROM Customers
	WHERE NOT CustomerId < 50;

/* INSERT INTO */
INSERT INTO nome_da_tabela (coluna1, coluna2, coluna3, ...)
VALUES
(dado_coluna1, dado_coluna2, dado_coluna3, ...),
(dado_coluna1, dado_coluna2, dado_coluna3, ...),
(dado_coluna1, dado_coluna2, dado_coluna3, ...);

-- 	EXEMPLOS:

	INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
	VALUES
	('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),
	('Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway'),
	('Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');

/* Valores NULL (Campos em Branco) */
-- IS NULL
SELECT nome_colunas
FROM nome_tabela
WHERE nome_coluna IS NULL;

-- IS NOT NULL
SELECT nome_colunas
FROM nome_tabela
WHERE nome_coluna IS NOT NULL;

-- 	EXEMPLOS:
	
	SELECT CustomerName, ContactName, Address
	FROM Customers
	WHERE Address IS NULL;
	
	SELECT CustomerName, ContactName, Address
	FROM Customers
	WHERE Address IS NOT NULL;

/* UPDATE */
UPDATE nome_da_tabela
SET coluna1 = valor1, coluna2 = valor2
WHERE condição

-- 	EXEMPLOS:

	UPDATE Customers
	SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
	WHERE CustomerID = 1;

	-- É a WHEREcláusula que determina quantos registros serão atualizados.
	
	/* A seguinte instrução SQL atualizará o ContactName para 
	"Juan" em todos os registros onde o país é "México": */
	UPDATE Customers
	SET ContactName = 'Juan'
	WHERE Country = 'Mexico';

/* DELETE */
DELETE FROM nome_da_tabela WHERE condição;

-- 	EXEMPLO:
	
	-- A seguinte instrução SQL exclui o cliente "Alfreds Futterkiste" da tabela "Clientes":
	DELETE FROM Customers WHERE CustomerName = 'Alfreds Futterkiste';

	-- Excluir todas as linhas de uma tabela sem excluir a tabela inteira.
	DELETE FROM nome_da_tabela;
	
	-- Exclui todas as linhas da tabela "Customers".
	DELETE FROM Customers;
	
	-- Excluir tabela
	DROP TABLE Customers;
	
/* SELECT TOP */ -- Dependendo do Banco, a Syntax muda
-- Mostrar os 3 primeiros Registros da tabela
SELECT TOP 3 * FROM nome_da_tabela;

-- Selecionar 50% dos registros
SELECT TOP 50 PERCENT * FROM Customers;

-- Seleciona os três primeiros registros da tabela "Clientes", onde o país é "Alemanha" 
SELECT TOP 3 * FROM Customers WHERE Country = 'Germany';

-- Ordene o resultado em ordem alfabética inversa por CustomerName e retorne os 3 primeiros registros:
SELECT TOP 3 * FROM Customers
ORDER BY CustomerName DESC;

/* Agregação */ -- Valores NULL não contam
/* MIN() (Menor) | MAX() (Maior) */
SELECT MIN (nome_coluna)
FROM nome_tabela
WHERE condição;

SELECT MAX (nome_coluna)
FROM nome_tabela
WHERE condição;

-- 	EXEMPLO:

	-- Encontre o preço mais baixo na coluna Preço:
	SELECT MIN(Price)
	FROM Products;
	
	-- Encontre o preço mais alto na coluna Preço:
	SELECT MIN(Price)
	FROM Products;
	
/* COUNT() (Contagem) */
SELECT COUNT (nome_coluna)
FROM nome_tabela
WHERE condição;
	
-- 	EXEMPLO:

	-- Encontre o número de produtos em que Priceé maior que 20:
	SELECT COUNT(ProductID)
	FROM Products
	WHERE Price > 20;
	
	-- Ignorar Duplicados: Quantos preços diferentes existem na Productstabela?
	SELECT COUNT(DISTINCT Price)
	FROM Products;
	
	/* COUNT() com GROUP BY */
	/* Aqui, utilizamos a COUNT()função e a GROUP BY cláusula para 
	retornar o número de registros de cada categoria na tabela Produtos. */
	SELECT COUNT(*) AS [Number of records], CategoryID
	FROM Products
	GROUP BY CategoryID;

/* SUM() (SOMA) */
SELECT SUM(nome_coluna)
FROM nome_tabela
WHERE condição;

-- 	EXEMPLO:
	
	-- Retorne a soma de todos Quantity os campos da OrderDetailstabela
	SELECT SUM(Quantity)
	FROM OrderDetails;
	
	-- Retorne a soma do Quantity campo para o produto com ProductID11
	SELECT SUM(Quantity)
	FROM OrderDetails
	WHERE ProductId = 11;

	-- Multiplicar cada valor por 10
	SELECT SUM(Quantity * 10)
	FROM OrderDetails;

	-- Combine OrderDetails com Products, e use SUM()para encontrar o valor total
	SELECT SUM(Price * Quantity)
	FROM OrderDetails
	LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID;

/* AVG() (Média) */
SELECT AVG(nome_coluna)
FROM nome_tabela
WHERE condição;

--	EXEMPLO
	
	-- Calcule o preço médio de todos os produtos
	SELECT AVG(Price)
	FROM Products;
	
	-- Retorne o preço médio dos produtos da categoria 1:
	SELECT AVG(Price)
	FROM Products
	WHERE CategoryID = 1;
	
	-- Acima da Média
	-- Devolva todos os produtos com preço superior ao preço médio:
	SELECT * FROM Products
	WHERE price > (SELECT AVG(price) FROM Products);
	
	/* Aqui, utilizamos a AVG()função e a GROUP BYcláusula para 
	retornar o preço médio de cada categoria na tabela Produtos: */
	SELECT AVG(Price) AS AveragePrice, CategoryID
	FROM Products
	GROUP BY CategoryID;
	
/* LIKE */
SELECT coluna1, coluna2, ...
FROM nome_tabela
WHERE nome_coluna LIKE padrão;

-- EXEMPLO:

	/* O símbolo de porcentagem '%' representa zero, um ou vários caracteres.
	Selecione todos os clientes cujo nome começa com a letra "a": */
	SELECT * FROM Customers
	WHERE CustomerName LIKE 'a%';
	
	/* O sinal de sublinhado '_' representa um único caractere.
	Pode ser qualquer caractere ou número, mas cada um '_' 
	representa um, e apenas um, caractere. */
	SELECT * FROM Customers
	WHERE city LIKE 'L_nd__';
	
	-- Curinga %
	-- Retornar todos os clientes de uma cidade que contenha a letra 'L':
	SELECT * FROM Customers
	WHERE city LIKE '%L%';
	
	-- Retornar todos os clientes cujos nomes começam com 'La':
	SELECT * FROM Customers
	WHERE CustomerName LIKE 'La%';
	
	-- Pode ser combinado com AND ou OR
	SELECT * FROM Customers
	WHERE CustomerName LIKE 'a%' OR CustomerName LIKE 'b%';
	
	-- Retornar todos os clientes que terminam com 'a':
	SELECT * FROM Customers
	WHERE CustomerName LIKE '%a';
	
	-- Retornar todos os clientes que começam com "b" e terminam com "s":
	SELECT * FROM Customers
	WHERE CustomerName LIKE 'b%s';
	
	-- Retornar todos os clientes que contenham a frase 'ou'
	SELECT * FROM Customers
	WHERE CustomerName LIKE '%or%';
	
	/* Combinar curingas
	Retornar todos os clientes que começam com "a" e têm 
	pelo menos 3 caracteres: */
	SELECT * FROM Customers
	WHERE CustomerName LIKE 'a__%';
	
	-- Retorne todos os clientes que têm "r" na segunda posição:
	SELECT * FROM Customers
	WHERE CustomerName LIKE '_r%';
	
	/* Usando []*/
	-- Retornar todos os clientes que começam com "b", "s" ou "p":
	SELECT * FROM Customers
	WHERE CustomerName LIKE '[bsp]%';
	
	-- Retornar todos os clientes que começam com "a", "b", "c", "d", "e" ou "f":
	SELECT * FROM Customers
	WHERE CustomerName LIKE '[a-f]%';
	
/* IN */
SELECT nome_coluna(s)
FROM nome_da_tabela
WHERE nome_coluna IN (valor1, valor2, ...);

--	EXEMPLO:

	-- Devolva todos os clientes da 'Alemanha', 'França' ou 'Reino Unido'.
	SELECT * FROM Customers
	WHERE Country IN ('Germany', 'France', 'UK');
	
	-- Retornar todos os clientes que NÃO sejam da 'Alemanha', 'França' ou 'Reino Unido':
	SELECT * FROM Customers
	WHERE Country NOT IN ('Germany', 'France', 'UK');
	
	-- IN
	-- Retornar todos os clientes que possuem um pedido na tabela Pedidos :
	SELECT * FROM Customers
	WHERE CustomerID IN (SELECT CustomerID FROM Orders);
	
	-- NOT IN
	-- Retornar todos os clientes que NÃO fizeram nenhum pedido na tabela de Pedidos :
	SELECT * FROM Customers
	WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders);

/* BETWEEN */
SELECT nome_coluna(s)
FROM nome_da_tabela
WHERE nome_coluna BETWEEN valor1 AND valor2;

--	EXEMPLO:
	
	-- Seleciona todos os produtos com preço entre 10 e 20:
	SELECT * FROM Products
	WHERE Price BETWEEN 10 AND 20;
	
	-- Para exibir os produtos que estão fora do intervalo do exemplo anterior, use NOT BETWEEN:
	SELECT * FROM Products
	WHERE Price NOT BETWEEN 10 AND 20;
	
	/* A seguinte instrução SQL seleciona todos os produtos com preço 
	entre 10 e 20. Além disso, o CategoryID deve ser 1, 2 ou 3: */
	SELECT * FROM Products
	WHERE Price NOT BETWEEN 10 AND 20
	AND CategoryID IN (1,2,3);
	
	/* Datas
	A seguinte instrução SQL seleciona todos os pedidos com 
	uma data de pedido (OrderDate) entre '01 de julho de 1996' 
	e '31 de julho de 1996': */
	SELECT * FROM Orders
	WHERE OrderDate BETWEEN '07/01/1996' AND '07/31/1996';

/* AS (alias(apelido)) */
SELECT nome_coluna AS apelido_nome
FROM nome_da_tabela;

-- 	EXEMPLO:

	-- Um alias é criado com a AS palavra-chave.
	SELECT CustomerID AS ID
	FROM Customers;
	
	-- cria dois aliases, um para a coluna CustomerID e outro para a coluna CustomerName:
	SELECT CustomerID AS ID, CustomerName AS Customer
	FROM Customers;
	
	-- Utilizando "aspas duplas" para aliases com espaços:
	SELECT ProductName AS "My Great Products"
	FROM Products;
	
/* Junções JOIN */
/* INNER JOIN */
SELECT nome_coluna1, nome_coluna2, ... -- SELECT *
FROM tabela1
INNER JOIN tabela2
ON tabela1.coluna_em_comum = tabela2.coluna_em_comum;

-- 	EXEMPLO:

	SELECT Products.ProductID, Products.ProductName, Categories.CategoryName
	FROM Products
	INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID;
	
	-- JOIN é o mesmo que INNER JOIN:
	SELECT Products.ProductID, Products.ProductName, Categories.CategoryName
	FROM Products
	JOIN Categories ON Products.CategoryID = Categories.CategoryID;
	
	-- Dois INNER JOIN
	SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
	FROM ((Orders
	INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
	INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);
	
/* LEFT JOIN (LEFT OUTER JOIN)*/
SELECT nome_coluna1, nome_coluna2, ... -- SELECT *
FROM tabela1
LEFT JOIN tabela2
ON tabela1.coluna_em_comum = tabela2.coluna_em_comum;

--	EXEMPLO:

	SELECT Customers.CustomerName, Orders.OrderID
	FROM Customers
	LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
	ORDER BY Customers.CustomerName;
	
	/* Observação: A LEFT JOIN palavra-chave retorna todos os 
	registros da tabela da esquerda (Clientes), mesmo que não 
	haja correspondências na tabela da direita (Pedidos). */
	
/* RIGHT JOIN (RIGHT OUTER JOIN)*/
SELECT nome_coluna1, nome_coluna2, ... -- SELECT *
FROM tabela1
RIGHT JOIN tabela2
ON tabela1.coluna_em_comum = tabela2.coluna_em_comum;

--	EXEMPLO:

	SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
	FROM Orders
	RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
	ORDER BY Orders.OrderID;
	
	/* Observação: A RIGHT JOIN palavra-chave retorna todos os 
	registros da tabela da direita (Funcionários), mesmo que 
	não haja correspondências na tabela da esquerda (Pedidos). */

/* FULL JOIN (FULL OUTER JOIN) */
SELECT nome_coluna1, nome_coluna2, ... -- SELECT *
FROM table1
FULL OUTER JOIN table2
ON tabela1.coluna_em_comum = tabela2.coluna_em_comum;

-- 	EXEMPLO:

	SELECT Customers.CustomerName, Orders.OrderID
	FROM Customers
	FULL OUTER JOIN Orders ON Customers.CustomerID=Orders.CustomerID
	ORDER BY Customers.CustomerName;
	
	/* Observação: A FULL OUTER JOIN palavra-chave retorna todos 
	os registros correspondentes de ambas as tabelas, 
	independentemente de a outra tabela também corresponder 
	ou não. Portanto, se houver linhas em "Clientes" que não 
	tenham correspondência em "Pedidos", ou se houver linhas 
	em "Pedidos" que não tenham correspondência em "Clientes", 
	essas linhas também serão listadas. */
	
/* UNION */
SELECT nome_coluna(s) FROM tabela1
UNION
SELECT nome_coluna(s) FROM tabela2;

-- 	EXEMPLO:

	/* A seguinte instrução SQL retorna as cidades (apenas 
	valores distintos) das tabelas "Clientes" e "Fornecedores": */
	SELECT City FROM Customers
	UNION
	SELECT City FROM Suppliers
	ORDER BY City;
	
	/* Observação: Se alguns clientes ou fornecedores tiverem a 
	mesma cidade, cada cidade será listada apenas uma vez, 
	pois UNIONa função seleciona apenas valores distintos. 
	Use a opção UNION ALLpara selecionar também valores duplicados!
	
	A seguinte instrução SQL retorna as cidades alemãs 
	(apenas valores distintos) das tabelas "Clientes" e 
	"Fornecedores": */
	SELECT City, Country FROM Customers
	WHERE Country='Germany'
	UNION
	SELECT City, Country FROM Suppliers
	WHERE Country='Germany'
	ORDER BY City;
	
/* UNION ALL */
SELECT nome_coluna(s) FROM tabela1
UNION ALL
SELECT nome_coluna(s) FROM tabela2;
	
-- 	EXEMPLO:
	
	/* A seguinte instrução SQL retorna as cidades (incluindo 
	valores duplicados) das tabelas "Clientes" e "Fornecedores": */
	SELECT City FROM Customers
	UNION ALL
	SELECT City FROM Suppliers
	ORDER BY City;