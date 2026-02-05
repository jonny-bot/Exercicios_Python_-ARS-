-- Criar A Base de Dados
create database analise_vendas;

-- Selecionar a Base de Dados
use analise_vendas;

-- =========================
-- Criação das Planilhas
-- =========================

-- =========================
-- Criar tabela de clientes
-- =========================
CREATE TABLE Clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(20),
    cidade VARCHAR(50),
    estado VARCHAR(50)
);

INSERT INTO Clientes (nome, email, telefone, cidade, estado)
VALUES 
('Maria Silva', 'maria.silva@email.com', '119999999', 'São Paulo', 'SP'),
('João Santos', 'joao.santos@email.com', '119888888', 'Santo André', 'SP'),
('Carla Pereira', 'carla.pereira@email.com', '219777777', 'Rio de Janeiro', 'RJ'),
('Pedro Oliveira', 'pedro.oliveira@email.com', '319666666', 'Belo Horizonte', 'MG'),
('Ana Costa', 'ana.costa@email.com', '419555555', 'Curitiba', 'PR'),
('Lucas Almeida', 'lucas.almeida@email.com', '519444444', 'Porto Alegre', 'RS'),
('Fernanda Rocha', 'fernanda.rocha@email.com', '619333333', 'Brasília', 'DF'),
('Rafael Lima', 'rafael.lima@email.com', '719222222', 'Salvador', 'BA');

-- =========================
-- Criar tabela de produtos
-- =========================
CREATE TABLE Produtos (
    produto_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    categoria VARCHAR(50),
    preco DECIMAL(10,2)
);

INSERT INTO Produtos (nome, categoria, preco)
VALUES
('Notebook Dell Inspiron', 'Eletrônicos', 3500.00),
('Mouse Logitech', 'Acessórios', 120.00),
('Cadeira Gamer ThunderX3', 'Móveis', 1250.00),
('Smartphone Samsung Galaxy S21', 'Eletrônicos', 4200.00),
('Teclado Mecânico Redragon', 'Acessórios', 350.00),
('Monitor LG 27"', 'Eletrônicos', 1800.00),
('Headset HyperX Cloud II', 'Acessórios', 600.00),
('Impressora HP Deskjet', 'Eletrônicos', 750.00);

-- =========================
-- Criar tabela de pedidos
-- =========================
CREATE TABLE Pedidos (
    pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT,
    data_pedido DATE,
    valor_total DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id)
);

INSERT INTO Pedidos (cliente_id, data_pedido, valor_total)
VALUES
(1, '2026-01-15', 3620.00),
(2, '2026-01-20', 1250.00),
(3, '2026-01-25', 4320.00),
(4, '2026-02-01', 1950.00),
(5, '2026-02-02', 4800.00),
(6, '2026-02-03', 750.00),
(7, '2026-02-04', 600.00),
(8, '2026-02-05', 5300.00);

-- =========================
-- Criar tabela de itens do pedido
-- =========================
CREATE TABLE Itens_Pedido (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    pedido_id INT,
    produto_id INT,
    quantidade INT,
    preco_unitario DECIMAL(10,2),
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(pedido_id),
    FOREIGN KEY (produto_id) REFERENCES Produtos(produto_id)
);

INSERT INTO Itens_Pedido (pedido_id, produto_id, quantidade, preco_unitario)
VALUES
(1, 1, 1, 3500.00),
(1, 2, 1, 120.00),
(2, 3, 1, 1250.00),
(3, 4, 1, 4200.00),
(3, 2, 1, 120.00),
(4, 5, 1, 350.00),
(4, 6, 1, 1600.00),
(5, 1, 1, 3500.00),
(5, 7, 2, 600.00),
(6, 8, 1, 750.00),
(7, 7, 1, 600.00),
(8, 4, 1, 4200.00),
(8, 6, 1, 1100.00);