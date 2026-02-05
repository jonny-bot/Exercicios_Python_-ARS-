-- =========================
-- Criação Tabela Produto
-- =========================
CREATE TABLE produtos (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome_produto VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    preco_unitario DECIMAL(10,2) NOT NULL
);

-- ===================================
-- Inserir dados na Tabela Produto
-- ===================================
INSERT INTO produtos (nome_produto, categoria, preco_unitario)
VALUES
('Notebook Dell Inspiron', 'Eletrônicos', 3500.00),
('Smartphone Samsung Galaxy', 'Eletrônicos', 2800.00),
('Televisão LG 50"', 'Eletrônicos', 2500.00),
('Mouse Logitech', 'Periféricos', 120.00),
('Teclado Mecânico Redragon', 'Periféricos', 250.00),
('Cadeira Gamer DXRacer', 'Móveis', 1500.00),
('Mesa de Escritório', 'Móveis', 800.00),
('Geladeira Brastemp', 'Eletrodomésticos', 3200.00),
('Fogão Consul 4 bocas', 'Eletrodomésticos', 1500.00),
('Micro-ondas Electrolux', 'Eletrodomésticos', 600.00),
('Camiseta Nike', 'Vestuário', 120.00),
('Calça Jeans Levis', 'Vestuário', 200.00),
('Tênis Adidas', 'Vestuário', 350.00),
('Relógio Casio', 'Acessórios', 400.00),
('Óculos de Sol Ray-Ban', 'Acessórios', 600.00),
('Livro "Clean Code"', 'Livros', 150.00),
('Livro "O Pequeno Príncipe"', 'Livros', 50.00),
('Arroz 5kg', 'Alimentos', 30.00),
('Feijão 1kg', 'Alimentos', 12.00),
('Café Pilão 500g', 'Alimentos', 18.00);

-- ===================================
-- Mostrar Dados da Tabela Produto
-- ===================================
select * from produtos;

-- ===================================
-- Mostrar Dados da Tabela Produtos
-- ===================================
drop table produtos;