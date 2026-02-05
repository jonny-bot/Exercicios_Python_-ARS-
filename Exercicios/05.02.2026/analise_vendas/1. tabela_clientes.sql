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
-- Mostrar Dados da Tabela Clientes
-- ===================================
drop table clientes;