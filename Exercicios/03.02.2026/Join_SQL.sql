-- Criar banco de dados
CREATE DATABASE Loja_Online;
USE Loja_Online;

-- Tabela de Clientes
CREATE TABLE Clientes (
    Cliente_ID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100),
    Email VARCHAR(100),
    Cidade VARCHAR(50)
);

-- Clientes
INSERT INTO Clientes (Nome, Email, Cidade) VALUES 
('Maria Silva', 'maria@email.com', 'São Paulo'), 
('João Santos', 'joao@email.com', 'Santo André'), 
('Ana Costa', 'ana@email.com', 'Campinas'), 
('Pedro Oliveira', 'pedro@email.com', 'Rio de Janeiro'), 
('Carla Mendes', 'carla@email.com', 'Belo Horizonte'), 
('Lucas Pereira', 'lucas@email.com', 'Curitiba'), 
('Fernanda Rocha', 'fernanda@email.com', 'Porto Alegre'), 
('Ricardo Lima', 'ricardo@email.com', 'Salvador'), 
('Juliana Alves', 'juliana@email.com', 'Fortaleza'), 
('Bruno Martins', 'bruno@email.com', 'Brasília');

-- Tabela de Produtos
CREATE TABLE Produtos (
    Produto_ID INT PRIMARY KEY AUTO_INCREMENT,
    Nome_Produto VARCHAR(100),
    Preco DECIMAL(10,2),
    Categoria VARCHAR(50)
);

-- Produtos
INSERT INTO Produtos (Nome_Produto, Preco, Categoria) VALUES 
('Notebook', 3500.00, 'Eletrônicos'), 
('Smartphone', 2000.00, 'Eletrônicos'), 
('Cafeteira', 300.00, 'Eletrodomésticos'), 
('Geladeira', 2500.00, 'Eletrodomésticos'), 
('Televisão 50"', 2800.00, 'Eletrônicos'), 
('Fone de Ouvido Bluetooth', 250.00, 'Acessórios'), 
('Mouse Gamer', 150.00, 'Acessórios'), 
('Livro - SQL para Iniciantes', 80.00, 'Livros'), 
('Tênis Esportivo', 350.00, 'Moda'), 
('Relógio de Pulso', 500.00, 'Moda');

-- Tabela de Pedidos
CREATE TABLE Pedidos (
    Pedido_ID INT PRIMARY KEY AUTO_INCREMENT,
    Cliente_ID INT,
    Data_Pedido DATE,
    FOREIGN KEY (Cliente_ID) REFERENCES Clientes(Cliente_ID)
);

-- Pedidos
INSERT INTO Pedidos (Cliente_ID, Data_Pedido) VALUES 
(1, '2026-02-01'), 
(2, '2026-02-02'), 
(3, '2026-02-03'), 
(4, '2026-02-04'), 
(5, '2026-02-05'), 
(6, '2026-02-06'), 
(7, '2026-02-07'), 
(8, '2026-02-08'), 
(9, '2026-02-09'), 
(10, '2026-02-10');

-- Tabela de Itens do Pedido (ligação entre Pedidos e Produtos)
CREATE TABLE Itens_Pedido (
    Item_ID INT PRIMARY KEY AUTO_INCREMENT,
    Pedido_ID INT,
    Produto_ID INT,
    Quantidade INT,
    FOREIGN KEY (Pedido_ID) REFERENCES Pedidos(Pedido_ID),
    FOREIGN KEY (Produto_ID) REFERENCES Produtos(Produto_ID)
);

-- Itens do Pedido
INSERT INTO Itens_Pedido (Pedido_ID, Produto_ID, Quantidade) VALUES
(1, 1, 1), -- Maria comprou 1 Notebook 
(1, 3, 2), -- Maria comprou 2 Cafeteiras 
(2, 2, 1), -- João comprou 1 Smartphone 
(3, 5, 1), -- Ana comprou 1 Televisão 50" 
(4, 7, 2), -- Pedro comprou 2 Mouses Gamer 
(5, 9, 1), -- Carla comprou 1 Tênis Esportivo 
(6, 4, 1), -- Lucas comprou 1 Geladeira 
(7, 6, 3), -- Fernanda comprou 3 Fones Bluetooth 
(8, 8, 2), -- Ricardo comprou 2 Livros SQL 
(9, 10, 1); -- Juliana comprou 1 Relógio de Pulso

-- Mostrar Tabela Clientes
select * from clientes;

-- Mostrar Tabela Itens Pedidos
select * from itens_pedido;

-- Mostrar Tabela Pedidos
select * from pedidos;

-- Mostrar Tabela Produtos
select * from produtos;

select *
from produtos
join itens_pedido
on produtos.Produto_ID = itens_pedido.Produto_ID