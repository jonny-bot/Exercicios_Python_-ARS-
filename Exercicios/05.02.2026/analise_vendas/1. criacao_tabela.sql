-- Exemplo de Criação de Tabela 
CREATE TABLE nome_tabela (
    id INT PRIMARY KEY,                        						-- Identificador único
    nome VARCHAR(100) NOT NULL,                						-- Nome obrigatório
    email VARCHAR(150) UNIQUE,                 						-- Não pode repetir
    idade INT CHECK (idade >= 18),             						-- Apenas maiores de 18
    data_pedido DATE DEFAULT (CURRENT_DATE),   						-- Valor padrão: hoje
    data_pedido_data_hora TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),	-- Valor padrão: data e hora de hoje
    ativo BOOLEAN DEFAULT TRUE                 						-- Status padrão: ativo
);

-- inserção de Teste
INSERT INTO nome_tabela (id, nome, email, idade)
VALUES
(1, 'Maria Silva', 'maria@email.com', 30),
(2, 'João Souza', 'joao@email.com', 25);
select * from nome_tabela;