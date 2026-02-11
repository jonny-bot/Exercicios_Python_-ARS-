INSERT INTO Clientes (nome, email, telefone, endereco)
VALUES 
('Maria Silva', 'maria.silva@email.com', '11987654321', 'Rua das Flores, 123 - São Paulo'),
('João Pereira', 'joao.pereira@email.com', '11912345678', 'Av. Paulista, 456 - São Paulo'),
('Ana Costa', 'ana.costa@email.com', '21998765432', 'Rua Atlântica, 789 - Rio de Janeiro'),
('Carlos Souza', 'carlos.souza@email.com', '31987654321', 'Rua Minas, 321 - Belo Horizonte');

INSERT INTO Categorias (nome, descricao)
VALUES 
('Eletrônicos', 'Produtos de tecnologia e eletrônicos'),
('Moda', 'Roupas e acessórios'),
('Casa', 'Itens para casa e decoração'),
('Esportes', 'Artigos esportivos');

INSERT INTO Produtos (nome, descricao, preco, estoque, categoria_id)
VALUES 
('Smartphone Galaxy S25', 'Celular Samsung última geração', 4500.00, 50, 1),
('Notebook Dell XPS 15', 'Notebook de alto desempenho', 9500.00, 30, 1),
('Camisa Polo Lacoste', 'Camisa polo masculina', 350.00, 100, 2),
('Tênis Nike Air Zoom', 'Tênis esportivo para corrida', 600.00, 80, 4),
('Sofá Retrátil 3 lugares', 'Sofá confortável para sala', 2500.00, 20, 3);

INSERT INTO Pedidos (cliente_id, status, valor_total)
VALUES 
(1, 'Pago', 4850.00),
(2, 'Pendente', 9500.00),
(3, 'Pago', 950.00),
(4, 'Cancelado', 2500.00);

INSERT INTO Itens_Pedido (pedido_id, produto_id, quantidade, preco_unitario)
VALUES 
(1, 1, 1, 4500.00), -- Smartphone
(1, 3, 1, 350.00),  -- Camisa Polo
(2, 2, 1, 9500.00), -- Notebook
(3, 4, 1, 600.00),  -- Tênis Nike
(3, 3, 1, 350.00),  -- Camisa Polo
(4, 5, 1, 2500.00); -- Sofá

INSERT INTO Pagamentos (pedido_id, metodo, valor, status)
VALUES 
(1, 'Cartão', 4850.00, 'Aprovado'),
(2, 'Pix', 9500.00, 'Pendente'),
(3, 'Boleto', 950.00, 'Aprovado'),
(4, 'Cartão', 2500.00, 'Recusado');
