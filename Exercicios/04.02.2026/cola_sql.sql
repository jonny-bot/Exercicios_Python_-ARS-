-- ============================================
-- COLA COMPLETA DE SQL PARA ESTUDOS
-- ============================================

-- ================================
-- 1. SELEÇÃO DE DADOS
-- ================================
SELECT * FROM tabela;                  -- Seleciona todas as colunas
SELECT coluna1, coluna2 FROM tabela;   -- Seleciona colunas específicas
SELECT coluna1 AS novo_nome FROM tabela; -- Renomeia coluna com alias

-- ================================
-- 2. FILTRAGEM
-- ================================
SELECT * FROM tabela WHERE coluna = 'valor'; -- Filtra registros
-- Operadores: =, <>, >, <, >=, <=
SELECT * FROM tabela WHERE coluna1 = 'x' AND coluna2 > 10; -- Combina condições
SELECT * FROM tabela WHERE coluna BETWEEN 10 AND 20;        -- Intervalo
SELECT * FROM tabela WHERE coluna IN ('A','B','C');         -- Lista de valores
SELECT * FROM tabela WHERE coluna LIKE 'Jo%';               -- Começa com Jo
SELECT * FROM tabela WHERE coluna LIKE '%ão';               -- Termina com ão

-- ================================
-- 3. ORDENAÇÃO E LIMITE
-- ================================
SELECT * FROM tabela ORDER BY coluna ASC;   -- Ordena crescente
SELECT * FROM tabela ORDER BY coluna DESC;  -- Ordena decrescente
SELECT * FROM tabela LIMIT 10;              -- Limita a 10 registros

-- ================================
-- 4. FUNÇÕES DE AGREGAÇÃO
-- ================================
SELECT COUNT(*) FROM tabela;       -- Conta registros
SELECT AVG(coluna) FROM tabela;    -- Média
SELECT SUM(coluna) FROM tabela;    -- Soma
SELECT MIN(coluna) FROM tabela;    -- Menor valor
SELECT MAX(coluna) FROM tabela;    -- Maior valor

-- ================================
-- 5. AGRUPAMENTO
-- ================================
SELECT coluna, COUNT(*) 
FROM tabela 
GROUP BY coluna;                   -- Agrupa por coluna

SELECT coluna, COUNT(*) 
FROM tabela 
GROUP BY coluna
HAVING COUNT(*) > 5;               -- Filtra grupos

-- ================================
-- 6. JUNÇÕES (JOINS)
-- ================================
SELECT a.coluna, b.coluna
FROM tabelaA a
INNER JOIN tabelaB b ON a.id = b.id;   -- INNER JOIN

SELECT a.coluna, b.coluna
FROM tabelaA a
LEFT JOIN tabelaB b ON a.id = b.id;    -- LEFT JOIN

SELECT a.coluna, b.coluna
FROM tabelaA a
RIGHT JOIN tabelaB b ON a.id = b.id;   -- RIGHT JOIN

-- ================================
-- 7. MANIPULAÇÃO DE DADOS
-- ================================
INSERT INTO tabela (coluna1, coluna2) VALUES ('valor1','valor2'); -- Inserir
UPDATE tabela SET coluna1 = 'novo_valor' WHERE id = 1;             -- Atualizar
DELETE FROM tabela WHERE id = 1;                                   -- Deletar

-- ================================
-- 8. FUNÇÕES DE JANELA (AVANÇADO)
-- ================================
SELECT coluna,
       ROW_NUMBER() OVER (ORDER BY coluna) AS num_linha,   -- Numeração
       RANK() OVER (ORDER BY coluna) AS ranking,           -- Ranking
       SUM(coluna) OVER (PARTITION BY grupo) AS soma_por_grupo -- Soma por grupo
FROM tabela;

-- ============================================
-- COLA DE CRIAÇÃO DE TABELAS
-- ============================================

-- ================================
-- 1. TABELA SIMPLES
-- ================================
CREATE TABLE clientes (
    id INT PRIMARY KEY,          -- chave primária
    nome VARCHAR(100) NOT NULL,  -- texto até 100 caracteres, obrigatório
    email VARCHAR(150) UNIQUE    -- não pode repetir
);

-- ================================
-- 2. TIPOS DE DADOS COMUNS
-- ================================
CREATE TABLE produtos (
    id INT PRIMARY KEY AUTO_INCREMENT, -- numeração automática
    nome VARCHAR(200) NOT NULL,        -- texto
    preco DECIMAL(10,2) NOT NULL,      -- número com 2 casas decimais
    estoque INT DEFAULT 0,             -- valor padrão
    criado_em DATE,                    -- apenas data
    atualizado_em TIMESTAMP            -- data e hora
);

-- ================================
-- 3. CHAVES ESTRANGEIRAS
-- ================================
CREATE TABLE pedidos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    data_pedido DATE NOT NULL,
    valor_total DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) -- chave estrangeira
);

-- ================================
-- 4. RESTRIÇÕES
-- ================================
CREATE TABLE funcionarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    salario DECIMAL(10,2) CHECK (salario > 0), -- restrição: salário positivo
    cargo VARCHAR(50) NOT NULL,
    departamento VARCHAR(50) DEFAULT 'Geral'
);

-- ================================
-- 5. ÍNDICES
-- ================================
CREATE TABLE vendas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL,
    data_venda DATE NOT NULL,
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

CREATE INDEX idx_venda_data ON vendas(data_venda); -- índice para buscas rápidas

-- ================================
-- 6. CHAVE COMPOSTA
-- ================================
CREATE TABLE curso_aluno (
    curso_id INT NOT NULL,
    aluno_id INT NOT NULL,
    PRIMARY KEY (curso_id, aluno_id), -- chave composta
    FOREIGN KEY (curso_id) REFERENCES cursos(id),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
);

-- ================================
-- 7. TABELA TEMPORÁRIA
-- ================================
CREATE TEMPORARY TABLE temp_relatorio (
    id INT,
    descricao VARCHAR(200)
);

-- ================================
-- 8. ENUM (MySQL)
-- ================================
CREATE TABLE status_pedido (
    id INT PRIMARY KEY AUTO_INCREMENT,
    status ENUM('Pendente','Pago','Cancelado') NOT NULL
);
