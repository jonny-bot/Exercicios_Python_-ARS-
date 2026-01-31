-- Resumo

-- ============================================================
-- ARQUIVO DE RESUMO: COMANDOS PRINCIPAIS DO MYSQL
-- ============================================================

-- -------------------------------
-- 1. GERENCIAMENTO DE BANCO DE DADOS
-- -------------------------------

-- Criar um banco de dados
CREATE DATABASE exemplo_db;

-- Usar um banco de dados
USE exemplo_db;

-- Apagar um banco de dados
DROP DATABASE exemplo_db;

-- -------------------------------
-- 2. GERENCIAMENTO DE TABELAS
-- -------------------------------

-- Criar uma tabela
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY, -- chave primária com incremento automático
    nome VARCHAR(100),                 -- campo de texto
    email VARCHAR(100),                -- campo de texto
    idade INT                          -- campo numérico
);

-- Alterar tabela (exemplo: adicionar coluna)
ALTER TABLE clientes ADD telefone VARCHAR(20);

-- Apagar tabela
DROP TABLE clientes;

-- -------------------------------
-- 3. MANIPULAÇÃO DE DADOS (CRUD)
-- -------------------------------

-- Inserir dados
INSERT INTO clientes (nome, email, idade) 
VALUES ('João', 'joao@email.com', 30);

-- Consultar dados
SELECT * FROM clientes; -- retorna todos os registros
SELECT nome, idade FROM clientes WHERE idade > 25; -- com filtro

-- Atualizar dados
UPDATE clientes SET idade = 31 WHERE id = 1;

-- Deletar dados
DELETE FROM clientes WHERE id = 1;

-- -------------------------------
-- 4. FILTROS E ORDENAÇÃO
-- -------------------------------

-- Ordenar resultados
SELECT * FROM clientes ORDER BY idade DESC;

-- Limitar resultados
SELECT * FROM clientes LIMIT 5;

-- Usar condições
SELECT * FROM clientes WHERE idade BETWEEN 20 AND 40;
SELECT * FROM clientes WHERE nome LIKE 'J%'; -- nomes que começam com J

-- -------------------------------
-- 5. FUNÇÕES COMUNS
-- -------------------------------

-- Contar registros
SELECT COUNT(*) FROM clientes;

-- Média, Máximo e Mínimo
SELECT AVG(idade), MAX(idade), MIN(idade) FROM clientes;

-- -------------------------------
-- 6. RELACIONAMENTOS (JOINS)
-- -------------------------------

-- Inner Join (apenas correspondências)
SELECT clientes.nome, pedidos.valor
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;

-- Left Join (todos os clientes, mesmo sem pedidos)
SELECT clientes.nome, pedidos.valor
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;

-- -------------------------------
-- 7. CONTROLE DE USUÁRIOS
-- -------------------------------

-- Criar usuário
CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'senha';

-- Dar permissões
GRANT ALL PRIVILEGES ON exemplo_db.* TO 'usuario'@'localhost';

-- Atualizar permissões
FLUSH PRIVILEGES;

-- ============================================================
-- FIM DO RESUMO
-- ============================================================