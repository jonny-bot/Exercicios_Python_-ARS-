-- 1. Clientes
CREATE TABLE Clientes (
    cliente_id INT PRIMARY KEY IDENTITY(1,1),
    nome NVARCHAR(100) NOT NULL,
    email NVARCHAR(100) UNIQUE,
    telefone NVARCHAR(20),
    endereco NVARCHAR(MAX),
    data_cadastro DATE DEFAULT GETDATE()
);

-- 2. Categorias
CREATE TABLE Categorias (
    categoria_id INT PRIMARY KEY IDENTITY(1,1),
    nome NVARCHAR(50) NOT NULL,
    descricao NVARCHAR(MAX)
);

-- 3. Produto
CREATE TABLE Produtos (
    produto_id INT PRIMARY KEY IDENTITY(1,1),
    nome NVARCHAR(100) NOT NULL,
    descricao NVARCHAR(MAX),
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES Categorias(categoria_id)
);

-- 4. Pedido
CREATE TABLE Pedidos (
    pedido_id INT PRIMARY KEY IDENTITY(1,1),
    cliente_id INT NOT NULL,
    data_pedido DATETIME DEFAULT GETDATE(),
    status NVARCHAR(20) CHECK (status IN ('Pendente','Pago','Cancelado','Enviado')),
    valor_total DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id)
);

-- 5. Itens_Pedido
CREATE TABLE Itens_Pedido (
    item_id INT PRIMARY KEY IDENTITY(1,1),
    pedido_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    subtotal AS (quantidade * preco_unitario) PERSISTED,
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(pedido_id),
    FOREIGN KEY (produto_id) REFERENCES Produtos(produto_id)
);

-- 6. Pagamentos
CREATE TABLE Pagamentos (
    pagamento_id INT PRIMARY KEY IDENTITY(1,1),
    pedido_id INT NOT NULL,
    metodo NVARCHAR(20) CHECK (metodo IN ('Cartão','Pix','Boleto','Transferência')),
    valor DECIMAL(10,2) NOT NULL,
    data_pagamento DATETIME DEFAULT GETDATE(),
    status NVARCHAR(20) CHECK (status IN ('Aprovado','Recusado','Pendente')),
    FOREIGN KEY (pedido_id) REFERENCES Pedidos(pedido_id)
);
