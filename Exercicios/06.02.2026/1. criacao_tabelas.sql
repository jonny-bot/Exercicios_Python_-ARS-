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
-- Excluir Tabela Produtos
-- ===================================
drop table produtos;

-- =========================
-- Criação Tabela Clientes
-- =========================
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome_cliente VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    estado VARCHAR(50),
    sigla_estado CHAR(2)
);

-- ===================================
-- Inserir dados na Tabela Clientes
-- ===================================
INSERT INTO clientes (nome_cliente, email, telefone, estado, sigla_estado)
VALUES
('Maria Silva', 'maria.silva@email.com', '(11) 91234-5678', 'São Paulo', 'SP'),
('João Pereira', 'joao.pereira@email.com', '(21) 99876-5432', 'Rio de Janeiro', 'RJ'),
('Ana Costa', 'ana.costa@email.com', '(31) 98765-4321', 'Minas Gerais', 'MG'),
('Carlos Souza', 'carlos.souza@email.com', '(41) 97654-3210', 'Paraná', 'PR'),
('Fernanda Lima', 'fernanda.lima@email.com', '(51) 96543-2109', 'Rio Grande do Sul', 'RS'),
('Paulo Oliveira', 'paulo.oliveira@email.com', '(71) 95432-1098', 'Bahia', 'BA'),
('Juliana Santos', 'juliana.santos@email.com', '(85) 94321-0987', 'Ceará', 'CE'),
('Ricardo Almeida', 'ricardo.almeida@email.com', '(62) 93210-9876', 'Goiás', 'GO'),
('Beatriz Rocha', 'beatriz.rocha@email.com', '(48) 92109-8765', 'Santa Catarina', 'SC'),
('Lucas Fernandes', 'lucas.fernandes@email.com', '(95) 91098-7654', 'Roraima', 'RR');

-- ===================================
-- Mostrar Dados da Tabela Clientes
-- ===================================
select * from clientes;

-- ===================================
-- Excluir Tabela Clientes
-- ===================================
drop table clientes;

-- =========================
-- Criação Tabela Pedido
-- =========================
CREATE TABLE pedidos (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_produto INT NOT NULL,
    id_cliente INT NOT NULL,
    quantidade_comprada INT NOT NULL,
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- ===================================
-- Inserir dados na Tabela Pedido
-- ===================================
INSERT INTO pedidos (id_produto, id_cliente, quantidade_comprada)
VALUES
(14, 5, 1),
(7, 8, 2),
(2, 1, 1),
(19, 10, 5),
(8, 9, 1),
(11, 6, 4),
(3, 4, 1),
(20, 1, 2),
(6, 7, 1),
(15, 6, 1),
(9, 10, 3),
(1, 2, 1),
(18, 9, 2),
(5, 6, 1),
(12, 3, 1),
(4, 2, 3),
(17, 9, 3),
(10, 1, 1),
(13, 7, 1),
(16, 7, 2),
(2, 3, 2),
(7, 4, 1),
(19, 10, 4),
(15, 8, 2),
(9, 5, 2),
(11, 2, 2),
(20, 10, 2),
(3, 2, 1),
(8, 4, 1),
(5, 3, 2),
(14, 7, 1),
(6, 3, 1),
(18, 9, 2),
(12, 6, 2),
(1, 1, 2),
(17, 8, 1),
(4, 5, 2),
(13, 4, 2),
(10, 5, 1),
(16, 8, 1);

-- ===================================
-- Mostrar Dados da Tabela Pedido
-- ===================================
select * from pedidos;

-- ===================================
-- Excluir Tabela Pedidos
-- ===================================
drop table pedidos;