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
(1, 1, 2),
(2, 1, 1),
(3, 2, 1),
(4, 2, 3),
(5, 3, 2),
(6, 3, 1),
(7, 4, 1),
(8, 4, 1),
(9, 5, 2),
(10, 5, 1),
(11, 6, 4),
(12, 6, 2),
(13, 7, 1),
(14, 7, 1),
(15, 8, 2),
(16, 8, 1),
(17, 9, 3),
(18, 9, 2),
(19, 10, 5),
(20, 10, 2),
(1, 2, 1),
(2, 3, 2),
(3, 4, 1),
(4, 5, 2),
(5, 6, 1),
(6, 7, 1),
(7, 8, 2),
(8, 9, 1),
(9, 10, 3),
(10, 1, 1),
(11, 2, 2),
(12, 3, 1),
(13, 4, 2),
(14, 5, 1),
(15, 6, 1),
(16, 7, 2),
(17, 8, 1),
(18, 9, 2),
(19, 10, 4),
(20, 1, 2);

-- ===================================
-- Mostrar Dados da Tabela Pedido
-- ===================================
select * from pedidos;

-- ===================================
-- Mostrar Dados da Tabela Pedidos
-- ===================================
drop table pedidos;