-- Selecionar o Tabela Inteira
select * from clientes;

-- Selecionar Algumas Colunas da Tabela:
select nome_cliente, email, estado from clientes;

-- Filtros - Parte 1:
select *
from clientes
where nome_cliente = 'Maria Silva';

-- Filtros - Parte 2:
select nome_cliente, email, estado
from clientes
where nome_cliente = 'Maria Silva';